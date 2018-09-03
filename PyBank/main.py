import csv

#The total number of months included in the dataset
#The total net amount of "Profit/Losses" over the entire period
#The average change in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

with open("budget_data.csv", 'r') as csvfile:
    bank_data = csv.reader(csvfile, delimiter=",")

    csv_header = next(bank_data)

    row_count = sum(1 for row in bank_data)

    print(row_count)
    