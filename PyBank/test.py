import csv

with open('budget_data.csv', 'r') as csv_file:

    csv_reader = csv.DictReader(csv_file)