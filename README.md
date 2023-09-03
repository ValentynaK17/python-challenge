# python-challenge
## Python Challenge - Data Analysis for Financial and Election Records
This repository contains Python scripts to analyze financial records of a company (PyBank) and election vote records to represent grouped calculated data per candidate and figure out votes distribution and the winner (PyPoll).
## Repository Structure
* PyBank: Directory containing the script, resources and analysis output for the financial data analysis.
* PyPoll: Directory containing the script, resources and analysis for the election data analysis.
## Installation
* Clone this repository to your local machine.
## Usage
### PyBank
* Navigate to the PyBank directory.
* Run the main.py script using python, which should be installed on your machine
* The financial analysis will be printed on the terminal and exported to an analysis directory as PyBank_Output.txt.
### PyPoll
* Navigate to the PyPoll directory.
* Run the main.py script.
* The election results will be printed on the terminal and exported to an analysis directory as PyPoll_Output.txt.
## Results
* PyBank: Analyzes financial records and calculates:
    * Total months in the dataset.
    * Net total amount of "Profit/Losses".
    * Changes in "Profit/Losses" and their average.
    * Greatest increase in profits (date and amount).
    * Greatest decrease in profits (date and amount).

As an example, for current resources, it would have the following output:
```Financial Analysis
---------------------------
Total Months: 86 
Total: $22564198 
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```
* PyPoll: Helps a small town modernize its vote-counting process by:
    * Calculating the total number of votes cast.
    * Listing candidates who received votes.
    * Calculating the percentage of votes each candidate won.
    * Calculating the total number of votes each candidate won.
    * Determining the winner of the election based on the popular vote.
      
As an example, for current resources, it would have the following output:
```Election Results
-------------------------
Total Votes: 369711 
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette 
-------------------------
```
