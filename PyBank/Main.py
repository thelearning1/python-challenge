#* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

#* Your task is to create a Python script that analyzes the records to calculate each of the following:

#  * The total number of months included in the dataset

#  * The net total amount of "Profit/Losses" over the entire period

 # * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  #* The greatest increase in profits (date and amount) over the entire period

#  * The greatest decrease in profits (date and amount) over the entire period

#* As an example, your analysis should look similar to the one below:

#  ```text
 # Financial Analysis
  #----------------------------
 # Total Months: 86
 # Total: $38382578
 # Average  Change: $-2315.12
 # Greatest Increase in Profits: Feb-2012 ($1926159)
 # Greatest Decrease in Profits: Sep-2013 ($-2196167)
 # ```

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.


#import libraries
import os
import csv

#read and define the csv path
csvpath = os.path.join('Resources', 'budget_data.csv')

#read the csv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # As each row is its own month, counting the number of rows after header will yield the number of months
    
    # Set row counter and totals to 0
    total = 0
    row_num = 0
    profitlist = []
    monthlist = []
    for row in csvreader:
        row_num +=1
        #sum the totals of the profit/losses column
        total += int(row[1])
        profitlist.append(int(row[1]))
        monthlist.append(row[0])
    pmin = min(profitlist)
    pmax = max(profitlist)
    print("Financial Analysis")
    print('------------------------')
    print(f"Total Months: {row_num}")
    print(f"Total: ${total}")
    
  
    #print(f"Greatest profit {pmax}")
    #print(f"Least profit {pmin}")


#determine the end of the profit list    
max_index = len(profitlist)

#establish a variable to reference index
i = 0

#create an empty list for the delta values
chg_list=[]

#populate the change list with the delta values
for item in profitlist:
  if i < max_index-1:
    chg_list.append((profitlist[i+1])-profitlist[i])
  i+=1

#calculate the average change, cast it as an integer and truncate it to two decimal places and print it
chgindex = len(chg_list)
chgavg = sum(chg_list)/chgindex
chgavg = round(chgavg,2)
print(f"Average Change ${chgavg}")

#print(chg_list)
increasemax = int(max(chg_list))
decreasemax = int(min(chg_list))
incmaxindex = chg_list.index(increasemax)+1
decmaxindex = chg_list.index(decreasemax)+1

print(f"{decmaxindex} and {incmaxindex}")
#match up the indices for the month list and the change list
incmaxmonth = monthlist[incmaxindex]
decmaxmonth = monthlist[decmaxindex]

print(f"Greatest Increase in Profits: {incmaxmonth} (${increasemax})")
print(f"Greatest Decrease in Profits: {decmaxmonth} (${decreasemax})")