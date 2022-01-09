# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#  1 The total number of votes cast

#  2 A complete list of candidates who received votes

#  3 The percentage of votes each candidate won

#  4 The total number of votes each candidate won

#  5 The winner of the election based on popular vote.

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#import libraries
import os
import csv

#read and define the csv path
csvpath = os.path.join('Resources', 'election_data.csv')

#read the csv
with open(csvpath) as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    #print(csv_reader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    #integer to store the total number of votes
    total_votes = 0

    #create an empty dictionary to add to in coming for loop
    vote_table = {}

    #loop through all rows of the csv and add the candidates as keys and the number of votes they got as values
    for row in csv_reader:
        
        #increment the total votes
        total_votes += 1

        #tell the coming for loop to reference the value in the third column
        c = str(row[2]) 

        #determines if a candidate is already in the dictionary vote_table, if they are not, it adds the candidate and sets their vote count to 1
        if c not in vote_table.keys():
            vote_table[c] = 1
        
        #if the candidate is already in the dictionary, it increments their vote value by 1
        else:
            vote_table[c] += 1

# create a list of candidates
candidates = [str(c) for c in vote_table.keys()]
# separate candidates list into something that looks nice
candidates = ", ".join(candidates)

#establish dummy value to overwrite in for loop
winner_votes = -1

#create an empty string for building onto 
cand_percs = ""

#loop through all the candidates in the dictionary vote_table
for candidate in vote_table.keys(): 

    # add the candidate and their vote percentages to the string cand_percs
    cand_percs += f" {candidate}:{round(100*(vote_table[candidate]/total_votes))}%"
    
    #Overwrites the winner_votes variable if the current candidate has more votes than the currently stored value
    if vote_table[candidate] > winner_votes:
        winner_votes = vote_table[candidate]

        #creates a snappy value that is only overwritten by a new candidate name if a new candidate has more votes
        winner = candidate

# Define the lines that need to be printed/exported
line_1 = f"Total Votes Cast: {total_votes}"
line_2 = f"Candidates in Election: {candidates}"
line_3 = f"Percentage of Votes per Candidate:{cand_percs}"     
line_4 = f"Votes Per Candidate: {vote_table}"
line_5 = f"The winner is... {winner}!!"  

#print the required lines to terminal
print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)

#export required lines to .txt file
with open ("Poll Results.txt", "w") as f:
    f.write(line_1+"\n")
    f.write(line_2+"\n")
    f.write(line_3+"\n")
    f.write(line_4+"\n")
    f.write(line_5+"\n")

    f.close