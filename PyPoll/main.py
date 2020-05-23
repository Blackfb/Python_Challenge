# Modules
import os
import csv
import collections
#Path for Resources Data
csvpath = os.path.join('Resources','election_data.csv')
Output_path = os.path.join("Analysis", "Output.txt")
# #Empty List
Candidate = []
#Open in read mode and skip to Header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
#Filling up Candidate List
    for row in csvreader:
        Candidate.append(row[2])
#Print to output
print("Election Results")
print("------------------------------------")
# Finding Total Votes
print(f'Total Votes: {len(Candidate)}')
print("------------------------------------")
#Using a Collection Module and making a dictionary and using the strengh of Python :)
counter = collections.Counter(Candidate)
for key,value in counter.items():
    print(f'{key} :{round((value/len(Candidate)*100))}.000% ({value})')
print("----------------------------------")
Winner = max(counter, key=counter.get)
print(f'Winner: {Winner}')
with open(Output_path, 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write(f'Total Votes: {len(Candidate)}\n')
    text.write("---------------------------------------\n")
    for key,value in counter.items():
     text.write(f"{key} :{round((value / len(Candidate) * 100))}.000% ({value})\n")
    Winner = max(counter, key=counter.get)
    text.write("-----------------------------------------\n")
    text.write(f'Winner: {Winner}')
