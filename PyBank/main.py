import os
import csv

budgetCSV = os.path.join('..', 'Resources', 'budget_data.csv')
output_file = os.path.join('budget_analysis.txt')

totalMonths = 0
totalNet = 0
previousNet = None
changeList = []
maxChange = None
maxMonth = None
minChange = None
minMonth = None

with open(budgetCSV) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    
    for row in reader:

        totalMonths += 1
        totalNet += int(row[1])
        
        if previousNet != None:
            netChange = int(row[1]) - previousNet
            changeList += [netChange]

            if maxChange == None or netChange > maxChange:
                maxChange = netChange
                maxMonth = row[0]

            if minChange == None or netChange < minChange:
                minChange = netChange
                minMonth = row[0]

        previousNet = int(row[1])

averageChange = sum(changeList) / len(changeList)

summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${totalNet}\n"
    f"Average  Change: ${averageChange:.2f}\n"
    f"Greatest Increase in Profits: {maxMonth} (${maxChange})\n"
    f"Greatest Decrease in Profits: {minMonth} (${minChange})\n"
    )

print(summary)

with open(output_file, 'w') as textfile:
    writer = textfile.write(summary)
