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
        
        diff = [-(monthly_dif_List[i]) + monthly_dif_List[i+1] for i in range(len(monthly_dif_List) -1)]
        
        avgPL = statistics.mean(diff)
    
        return(avgPL)

def find_best_month_amt(bankData):
    with open(bankData, 'r') as csvfile:
        bank_data = csv.DictReader(csvfile, delimiter=",")     
    
        monthly_dif_List = []
        difference = []

        for row in bank_data:
            monthly_dif_List.append(int(row['Profit/Losses']))

        difference = [-(monthly_dif_List[i]) + monthly_dif_List[i+1] for i in range(len(monthly_dif_List) -1)]
        maxMonth = max(difference)
 
        return(maxMonth)

def find_worst_month_amt(bankData):
    with open(bankData, 'r') as csvfile:
        bank_data = csv.DictReader(csvfile, delimiter=",")     
    
        monthly_dif_List = []
        difference = []
        for row in bank_data:
            monthly_dif_List.append(int(row['Profit/Losses']))

        difference = [-(monthly_dif_List[i]) + monthly_dif_List[i+1] for i in range(len(monthly_dif_List) -1)]
        minMonth = min(difference)

        return(minMonth)
    
def find_best_month(bankData, best_month):
    with open(bankData, 'r') as csvfile:
        bank_data = csv.DictReader(csvfile, delimiter=",")     

        max_list, date_list, differences = [], [], []

        for row in bank_data:
            max_list.append(int(row['Profit/Losses']))
            date_list.append(row['Date'])

        differences = [-(max_list[i]) + max_list[i+1] for i in range(len(max_list) -1)]

        data_counter = 0

        for a_diff in differences:
            data_counter +=1
            if a_diff == best_month:    
                return (date_list[data_counter])         
        

def find_worst_month(bankData, worst_month):
    with open(bankData, 'r') as csvfile:
        bank_data = csv.DictReader(csvfile, delimiter=",")     

        min_list, date_list, differences = [], [], []

        for row in bank_data:
            min_list.append(int(row['Profit/Losses']))
            date_list.append(row['Date'])

        differences = [-(min_list[i]) + min_list[i+1] for i in range(len(min_list) -1)]

        data_counter = 0

        for a_diff in differences:
            data_counter += 1
            if a_diff == worst_month:
                return (date_list[data_counter])
        
def print_to_file(data, pl_total, pl_change, good_month, bad_month,good_cal, bad_cal):
    with open("C:\\Users\\sallad\\Documents\\GitHub\\python-challenge\\pyBank\\financial_analysis.txt", "w") as text_file:
        print("Financial Analysis")
        print("-------------------------------------")
        print(f'Total Months: {data}', file=text_file)
        print(f'Total: ${pl_total}', file=text_file)
        print(f'Average Change: ${pl_change}', file=text_file)
        print(f'Greatest Increase in Profits: {good_cal} (${good_month})', file=text_file) 
        print(f'Greatest Decrease in Profits: {bad_cal} (${bad_month})', file=text_file)
        text_file.close()

def main():
    #define CSV path
    bank_data_file = 'C:\\Users\\sallad\\Documents\\GitHub\\python-challenge\\pyBank\\budget_data.csv'    

    #The total number of months included in the dataset
    data_items = findDataCount(bank_data_file)
    
    #The total net amount of "Profit/Losses" over the entire period
    profit_loss_total = findPLTotal(bank_data_file)
    
    #The average change in "Profit/Losses" between months over the entire period
    profit_loss_change = average_change_PL(bank_data_file)
    
    #The greatest increase in profits (amount) over the entire period
    most_profitable_month = find_best_month_amt(bank_data_file)
    
    #The greatest decrease in losses (amount) over the entire period
    least_profitable_month = find_worst_month_amt(bank_data_file)
        
    #The greatest increase in profits (date) over the entire period
    best_calendar_mth = find_best_month(bank_data_file, most_profitable_month)
    
    #The greatest decrease in losses (date) over the entire period
    worst_calendar_mth = find_worst_month(bank_data_file, least_profitable_month)
    
    print("Financial Analysis")
    print("-------------------------------------")
    print('Total Months: ' + str(data_items))
    print('Total: $' + str(profit_loss_total))
    print('Average Change: $' + str(profit_loss_change))
    print('Greatest Increase in Profits: ' + best_calendar_mth + " ($" + str(most_profitable_month)+ ")") 
    print('Greatest Decrease in Profits: ' + worst_calendar_mth + " ($" + str(least_profitable_month)+ ")")

    print_to_file(data_items, profit_loss_total, profit_loss_change, most_profitable_month, least_profitable_month, best_calendar_mth, worst_calendar_mth)    


main()


    