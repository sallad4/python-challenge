import csv
import statistics
from collections import Counter

def findDataCount(bankData):
    with open(bankData, 'r') as csvfile:
        bank_data = csv.DictReader(csvfile, delimiter=",")
           
        count = 0
        
        for _ in bank_data:
            count += 1

        return count

def findPLTotal(bankData):
    with open(bankData, 'r') as csvfile:
        bank_data = csv.DictReader(csvfile, delimiter=",")    
    
        plTotal = 0

        for row in bank_data:
            plTotal += int(row['Profit/Losses'])

        return plTotal

def average_change_PL(bankData):
    with open(bankData, 'r') as csvfile:
        bank_data = csv.DictReader(csvfile, delimiter=",")     

        monthly_dif_List = []
        diff = []

        for row in bank_data:
            monthly_dif_List.append(int(row['Profit/Losses']))

        diff = [monthly_dif_List[i] - monthly_dif_List[i+1] for i in range(len(monthly_dif_List) -1)]
        
        avgPL = statistics.mean(diff)
    
        return(avgPL)

def find_best_month_amt(bankData):
    with open(bankData, 'r') as csvfile:
        bank_data = csv.DictReader(csvfile, delimiter=",")     
    
        monthly_dif_List = []
        diff = []

        for row in bank_data:
            monthly_dif_List.append(int(row['Profit/Losses']))

        diff = [monthly_dif_List[i] - monthly_dif_List[i+1] for i in range(len(monthly_dif_List) -1)]
        maxMonth = max(diff) * -1
 
        return(maxMonth)

def find_worst_month_amt(bankData):
    with open(bankData, 'r') as csvfile:
        bank_data = csv.DictReader(csvfile, delimiter=",")     
    
        monthly_dif_List = []
        diff = []
        for row in bank_data:
            monthly_dif_List.append(int(row['Profit/Losses']))

        diff = [monthly_dif_List[i] - monthly_dif_List[i+1] for i in range(len(monthly_dif_List) -1)]
        minMonth = min(diff) * -1

        return(minMonth)
    
def find_best_month(bankData, bestMonth):
    with open(bankData, 'r') as csvfile:
        bank_data = csv.DictReader(csvfile, delimiter=",")

        for row in bank_data:
            if bestMonth == int(row['Profit/Losses']):
                return(row['Date'])

def find_worst_month(bankData, worstMonth):
    with open(bankData, 'r') as csvfile:
        bank_data = csv.DictReader(csvfile, delimiter=",")

        for row in bank_data:
            if worstMonth == int(row['Profit/Losses']):
                return(row['Date'])      
       
    
    
    #print(maxMonth)
    #print(minMonth)
    
    #plTotal = 0

    #for row in bankData:
    #   plTotal += int(row[1])
    
    #print(plTotal)

#The total number of months included in the dataset
#The total net amount of "Profit/Losses" over the entire period
#The average change in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#with open('pyBank/budget_data.csv', 'r') as csvfile:
#    bank_data = csv.DictReader(csvfile, delimiter=",")
    #next(bank_data)
    
#    for row in bank_data:
#        print(row['Profit/Losses'])
def main():

    bank_data_file = 'C:\\Users\\sallad\\Documents\\GitHub\\python-challenge\\pyBank\\budget_data.csv'    

    data_items = findDataCount(bank_data_file)
    print(data_items)

    profit_loss_total = findPLTotal(bank_data_file)
    print(profit_loss_total)

    profit_loss_change = average_change_PL(bank_data_file)
    print(profit_loss_change)

    most_profitable_month = find_best_month_amt(bank_data_file)
    print(most_profitable_month)

    least_profitable_month = find_worst_month_amt(bank_data_file)
    print(least_profitable_month)
    
    best_calendar_mth = find_best_month(bank_data_file, most_profitable_month)
    print(best_calendar_mth)

    worst_calendar_mth = find_worst_month(bank_data_file, least_profitable_month)
    print(worst_calendar_mth)

main()

    

 
    #findDataCount(bank_data)
    #findPLTotal(bank_data)

    