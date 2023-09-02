#separate function for reading from csv, which returns two lists: header and the one with actual data
def file_reading(file_path_input):
    import csv
    with open(file_path_input,"r",encoding="utf-8") as file_obj:
        file_obj_reader = csv.reader(file_obj,delimiter=",")
#separating header and the body with actual data into two lists
        return next(file_obj_reader), list(file_obj_reader)
    

#separating columns with data in separate lits
def column_split(list_input):
    if list_input!=[]:
        final=[]
        for j in range(len(list_input[0])): #assume that we have same lenght of list elements of input list, and it will define how many columns we have and how many lists in final list will be 
           column_list=[]
           for i in list_input:
               column_list.append(i[j]) # forming a list within final list by adding one by one value from a column at the end of list
           final.append(column_list) #appending resulting list(used to be column) as an item at the end to final list
        return final
    else: return None # in case we receive empty list, return respectively
    

#checking if there are duplicates in the list (using recursion) and returning true for existing duplicates, else false
def are_duplicates(list_input): 
    if list_input==[]: return False #checking edge case with empty list as an input + defining output for deepest recursion step
    elif list_input[0] in list_input[1:]: return True #checking if there is an item in the list (starting second item) that is the same as the first one
    else: return are_duplicates(list_input[1:]) #and then we compare each next item if there is identical one in the rest of the list after it


#generating list of deltas between consecutive input list's elements
def delta_list(list_input): 
    delta_l=[float(list_input[i])-float(list_input[i-1]) for i in range(1,len(list_input))] #list items are the difference between items in the original (list's item - previous list's item)
    return delta_l


#calculating the average within list's items
def list_average(list_input):
    if list_input!=[]: return round(sum(list_input)/len(list_input),2)
    else: return None


#identifying the maximum value among positive list's items and what are their positions in this list
def max_Positive (list_input):
    max_positive=0
    max_position=[] #in case all elements are equal or there are no positive items or list is empty
    #looking for a max, by comparing temporary max, with list's elements and selecting the bigger one as new max
    for i in range(len(list_input)):
        if list_input[i]>0 and list_input[i]>max_positive: max_positive=list_input[i] #skip list item=0, as it is not a positive one (profit), same for list item<0
    #position of max value as list for the case if there are several instances of same max positive value
    max_position=[i for i in range(len(list_input)) if max_positive!=0 and list_input[i]==max_positive]
    return max_positive, max_position #max_position is empty list if no positive items


#identifying the minimum value among negative list's items and what are their positions in this list
def min_Negative (list_input):
    min_negative=0
    min_position=[] #in case all elements are equal or no negative values (Loss) or empty list
    for i in range(len(list_input)): 
        if list_input[i]<0 and list_input[i]<min_negative: min_negative=list_input[i]
        #position of minimum negative as list for the case if there are several instances of same min negative value
    min_position=[i for i in range(len(list_input)) if min_negative!=0 and list_input[i]==min_negative]
    return min_negative, min_position #min_position is empty list if no negative values


#joins items from a list based on its position, incrementing position with +1 (for our task will be useful when there are several such dates with same max loss/profit)
def string_join(list_positions,list_data):
    if list_positions!=[]:
        fin_string=str(list_data[int(list_positions[0]+1)])
        for i in range(1,len(list_positions)): 
            fin_string+=(f", {list_data[int(list_positions[i]+1)] }")
    else: fin_string=""
    return fin_string

import os
#---------------------------------------------------------------------------------
#-------------------------------------PyBank--------------------------------------
#---------------------------------------------------------------------------------

file_path=os.path.join("PyBank","Resources","budget_data.csv")
header_list, data_lists=file_reading(file_path) #assume that file exists and at least header is present in it
#reserving separate string for all our outputs
Output_string=f"Financial Analysis\n---------------------------\n" 

if data_lists!=[]:
    date_column_list, profit_loss_column_list=column_split(data_lists) 
#assuming that we have accurate data with no duplicated mnths, which is currently the case
    if not are_duplicates(date_column_list):
         #we calculate the total number of months included in the dataset as simply a count of rows (without header)
         total_number_of_months=len(date_column_list)
         Output_string+=f"Total Months: {total_number_of_months} \n" #each time we have something new to output->add it to our reserved string
         #The net total amount of "Profit/Losses" over the entire period is a sum of "Profit/Losses" for all the listed mnths
         total_amount_ProfitLoss=0
         for i in range(total_number_of_months):
             total_amount_ProfitLoss+=int(profit_loss_column_list[i])
         Output_string+=f"Total: ${total_amount_ProfitLoss} \n"
#Looking for the changes in "Profit/Losses" over the entire period (per month)
         difference_list=delta_list(profit_loss_column_list)
         #calculating the average of changes in "Profit/Losses" over the entire period
         average_difference=list_average(difference_list)
        #then searching max positive and min negative among the above list of differences in order to find:
           #(1)The greatest increase in profits (positions of dates and amount) over the entire period
         max_Profit, max_profit_position = max_Positive(difference_list)
           #(2) and The greatest decrease in profits (positions of dates and amount) over the entire period 
           #respectively
         max_Loss, max_loss_position = min_Negative(difference_list)
         
        #and appending all the found value to our reserved string, notifying about possible edge cases if they are present in our data
         if average_difference != None:
             Output_string+=f"Average Change: ${average_difference}\n"
         else: Output_string+=f"There are no enough data to analyse difference (no data or single row)\n"
    
         dates_string=string_join(max_profit_position,date_column_list)
         if dates_string!="":
             Output_string+=f"Greatest Increase in Profits: {dates_string} (${int(max_Profit)})\n"
         else: Output_string+=f"There are no increases in Profits \n"

         dates_string=string_join(max_loss_position,date_column_list)
         if dates_string!="":
             Output_string+=f"Greatest Decrease in Profits: {dates_string} (${int(max_Loss)})\n" 
         else: Output_string+=f"There are no decreases in Profits \n"
        
    else: Output_string+=f"Review data to omit duplication in months\n"
else: Output_string+="No data to analyze\n"
print(Output_string)#print the analysis to the terminal

#export the above string with analysis results into the text file
new_file_path = os.path.join("PyBank","analysis","PyBank_Output.txt")
with open(new_file_path,"w")  as file_obj:
    file_obj.writelines(Output_string)