import os
import csv

#Set Path
csvpath = os.path.join('/Users/pmc/Desktop/GitHub/python-challenge/PyBank/Resources/budget_data.csv')

#Variables
total_months = 0
monthly_change = []
month_count = []
net_amount = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = 0
greatest_decrease_month = 0

#Open CSV File
with open(csvpath, newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    row = next(csvreader)

    #Calculate Total # on Months, Net Amout of Profit/Losses & Set Variables for Rows
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    #Read Each Row of Date After the Header
    for row in csvreader:

        #Calculate Total Number of Months included in Dataset
        total_months += 1
        #Calculate Net Amount of Profit/Losses over the entire period
        net_amount += int(row[1])

        #Calculate Change from current month to previous month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])

        #Calculate the Greatest Income
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        #Calculate the Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]
    #Calculate the Average & Date
    average_change = sum(monthly_change)/ len(monthly_change)

    highest = max(monthly_change)
    lowest = min(monthly_change)

#Print
print(f"Financial Analysis")
print(f"Total: ${net_amount}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest}")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")
print(f"Average Change: ${average_change: .2f}")
print(f"Total Months: {total_months}")

#File Write
output_file = os.path.join('/Users/pmc/Desktop/GitHub/python-challenge/PyBank/Analysis/results.text')

with open(output_file, 'w',) as txtfile:

    #Text File
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Total Months: {total_months}\n")



