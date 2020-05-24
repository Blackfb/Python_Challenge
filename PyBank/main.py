#Modules
import csv
import os
#Path for Resources Data
Csvpath = os.path.join('Resources','budget_data.csv')
Output_path = os.path.join("Analysis", "Output.txt")
#Empty List
Months = []
Amount = []
Difference = []
Prev = 0
#Open in read mode and skip to Header
with open(Csvpath, 'r') as Csvfile:
    Csv_reader = csv.reader(Csvfile, delimiter=',')
    Csv_header = next(Csv_reader)
#Filling up the empty list
    for row in Csv_reader:
        Months.append(row[0])
        Amount.append(row[1])
#Find Difference & make a list
        x = int(row[1]) - int(Prev)
        Prev = row[1]
        Difference.append(x)
# Using the zip function for parallel iteration
clean = zip(Months, Difference)
clean_lst = list(clean)
Difference.remove(Difference[0])
clean_lst.remove(clean_lst[0])
#Finding Profits,Total, Avg,Great. Inc. & Great. Dec.
total = sum(map(int, Amount))
average_change = sum(Difference) / len(Difference)
increase = max(Difference)
decrease = min(Difference)
Greatest_Increase = 0
Greatest_Decrease = 0
for row in clean_lst:
    if row[1] == increase:
        Greatest_Increase = row[0]
    if row[1] == decrease:
        Greatest_Decrease = row[0]
#First part for the Output and Second part for the text file
print(f'Financial Analysis')
print(f'------------------------------------')
print(f'Total Months: {len(Amount)}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {Greatest_Increase} ({increase})')
print(f'Greatest Decrease in Profits: {Greatest_Decrease} ({decrease})')
with open(Output_path, 'w') as text:
      text.write("Financial Analysis\n")
      text.write(f'------------------------------------\n')
      text.write(f'Total Votes: {len(Amount)}\n')
      text.write(f'Total: ${total}\n')
      text.write(f'Average Change: ${average_change:.2f}\n')
      text.write(f'Greatest Increase in Profits: {Greatest_Increase} ({increase})\n')
      text.write(f'Greatest Increase in Profits: {Greatest_Decrease} ({decrease})\n')
