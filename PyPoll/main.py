import os
import csv

#Set Path
csvpath = os.path.join('/Users/pmc/Desktop/GitHub/python-challenge/PyPoll/Resources/election_data.csv')

#Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#Open CSV File
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)

    for row in csvreader:
        
        #Total # of votes cast
        total_votes += 1
        
        #Total # of votes each candidate won
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            
    #Percentage of votes each candidate won
    kahn_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes
    
    #Winner of the election based On popular vote
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

#Print
print(f"Election Results")
print(f"Total Votes: {total_votes}")
print(f"Kahn: {kahn_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"Winner: {winner_name}")

#File Write
output_file = os.path.join('/Users/pmc/Desktop/GitHub/python-challenge/PyPoll/Analysis/results.text')

with open(output_file, 'w',) as txtfile:

#Text File
    txtfile.write(f"Election Results\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"Kahn: {kahn_percent:.3%}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    txtfile.write(f"Winner: {winner_name}\n")
