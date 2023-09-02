#separate function for reading from csv, which returns two lists: header and the one with actual data
def file_reading(file_path_input):
    import csv
    with open(file_path_input,"r",encoding="utf-8") as file_obj:
        file_obj_reader = csv.reader(file_obj,delimiter=",")
#separating header and the body with actual data into two lists
        return next(file_obj_reader), list(file_obj_reader)
    

#checking if there are duplicates in the list returning true for existing duplicates, else false
# source https://www.trainingint.com/how-to-find-duplicates-in-a-python-list.html#:~:text=Method%201%3A%20Using%20the%20length,Python%20program%20to%20check%20this.&text=mylist%20%3D%20%5B5%2C%203%2C,5%20%26%206%20are%20duplicate%20numbers.&text=As%20you%20can%20see%2C%20the,the%20myset%20length%20is%206.
def are_duplicates(list_input): 
    if len(list_input)!=len(set(list_input)): return True
    else: return False

#identifying the maximum value among positive list's items and their count
def max_Positives (list_input):
    max_positive=0
    max_items_count=0 #in case all elements are equal or there are no positive items or list is empty
    #looking for a max, by comparing temporary max, with list's elements and selecting the bigger one as new max
    for i in range(len(list_input)):
        if list_input[i]>0 and list_input[i]>max_positive: #skip list item=0, as it is not a positive one (profit), same for item<0
            max_positive=list_input[i]
    #find the count of max values
    for i in range(len(list_input)):
        if max_positive!=0 and list_input[i]==max_positive:
            max_items_count+=1
    return max_positive, max_items_count #max_position is empty list if no positive items

#returns only that column (from a list of lists), converted to a list, which has same index as defined in function input
def column_split(list_input,column_index):
    if column_index>(len(list_input[0])-1): return None #checking for column existense
    else:
        if list_input!=[]:
            column_list=[]
            for i in list_input:
                column_list.append(i[column_index]) # forming a list by adding one by one value from the desired column at the end of the list
            return column_list
        else: return None # in case we receive empty list, return respectively

import os

#---------------------------------------------------------------------------------
#-------------------------------------PyPoll--------------------------------------
#---------------------------------------------------------------------------------   
file_path=os.path.join("PyPoll","Resources","election_data.csv")
header_list, data_lists=file_reading(file_path) #assume that file exists and at least header is present in it
#set default value for output string, which will be further expanded with more data
Output_string=f"Election Results\n-------------------------\n"

if data_lists!=[]:
    #just in case, check if there are no duplicated ballots, so that we can warn about about not reliable data
    id_column_list=column_split(data_lists,0)
    if are_duplicates(id_column_list):
        Output_string+=f"WARNING: Data need to have Ballot ID mentioned not more than once to have reliable results. Currently it is not the case\n-------------------------\n"
    
    #calculating total count of votes, which is total count of rows, excluding header, assuming that ids are unique
    total_votes=len(data_lists)
    Output_string+=f"Total Votes: {total_votes} \n-------------------------\n"
    #composing complete list of candidates who received votes along with the total number of votes each candidate won using dictionary with count of votes per candidate
    candidate_dictionary=({f"{data_lists[0][2]}":1})
    for i in range(1,len(data_lists)): 
        if data_lists[i][2] in candidate_dictionary.keys():
            candidate_dictionary[f"{data_lists[i][2]}"]+=1 
        else: candidate_dictionary[f"{data_lists[i][2]}"]=1
    for i in candidate_dictionary.keys():
        #calculate The percentage of votes each candidate won: having votes per candidate and total number of votes is equals to 100*(votes per candidate)/(total number of votes)
        candidate_percentage_vote=round(100*candidate_dictionary.get(i)/total_votes,3) #if we are in this branch, then at least one vote is present, so no need to handle div 0 case 
        #and prepare to output the dictionary data along with percentage of votes
        Output_string+=f"{i}: {candidate_percentage_vote}% ({candidate_dictionary.get(i)})\n"  
    #looking for a winner: this is the one who has max count of votes, so we are searcing max among votes count(converting votes to a list)
    max_votes, count_max=max_Positives(list(candidate_dictionary.values()))
    if count_max>1: #just in case there are several winners, which is unlikely
        Output_string+=f"-------------------------\n Winners: " 
        winners_already_listed_count=0
        for i in candidate_dictionary.keys(): #per each key, which is candidate
            if candidate_dictionary.get(i)==max_votes: #we are looking if they are the one with max votes count
                winners_already_listed_count+=1  
                if winners_already_listed_count==count_max: #also we are checking if we found all the winners
                    Output_string+=f"{i} \n-------------------------"
                else: Output_string+=f"{i}, "
    else: 
        Output_string+=f"-------------------------\nWinner: " #branch for single winner
        for i in candidate_dictionary.keys():
            if candidate_dictionary.get(i)==max_votes: Output_string+=f"{i} \n-------------------------"
        #being sure that there is a single winner we could use simply max function with value as a key for search, e.g, max(candidate_dictionary, key=candidate_dictionary.get), as mentioned https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
else: Output_string+="No data to analyze\n"
print(Output_string) #print the analysis to the terminal

#export the above string with analysis results into the text file
new_file_path = os.path.join("PyPoll","analysis","PyPoll_Output.txt")
with open(new_file_path,"w")  as file_obj:
    file_obj.writelines(Output_string)