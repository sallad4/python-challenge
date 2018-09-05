import csv
import statistics

#def findDataCount(bankData):
    #bankDataCount = csv.reader(bankData, delimiter=",")
    
    #count = 0

    #for _ in bankData:
    #    count += 1

    #print(count)

#def findPLTotal(bankData):
    #bank_PL_data = csv.reader(bankData, delimiter=",")
    #next(bankData)

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

with open('pyBank/budget_data.csv', 'r') as csvfile:
    bank_data = csv.DictReader(csvfile, delimiter=",")
    
    count = 0

    for _ in bank_data:
        count += 1

    print(count)

with open('pyBank/budget_data.csv', 'r') as csvfile:
    bank_data = csv.DictReader(csvfile, delimiter=",")    
    
    plTotal = 0

    for row in bank_data:
        plTotal += int(row['Profit/Losses'])
    
    print(plTotal)

with open('pyBank/budget_data.csv', 'r') as csvfile:
    bank_data = csv.DictReader(csvfile, delimiter=",")     
    
    monthly_PL_List = []
    monthly_dif_List = []
    diff = [] 
    
    for row in bank_data:
        monthly_PL_List.append(int(row['Profit/Losses']))

    diff = [monthly_PL_List[i] - monthly_PL_List[i+1] for i in range(len(monthly_PL_List) -1)]
    maxMonth = max(diff)
    minMonth = min(diff)

    avgPL = statistics.mean(diff)
    
    print(avgPL)
    print(maxMonth)
    print(minMonth)

with open('pyBank/budget_data.csv', 'r') as csvfile:
    bank_data = csv.DictReader(csvfile, delimiter=",")     
    
    maxList, minList, dateList = [], [], []

    for row in bank_data:
        maxList.append(int(row['Profit/Losses']))
        minList.append(int(row['Profit/Losses']))
        dateList.append(row['Date'])
        
    maxMonth = max(maxList)
    minMonth = min(minList)

    counter = 0

    for i in maxList:
        if int(i) == maxMonth:    
            print(dateList[counter] + " " + str(maxMonth))
            break 
        counter +=1

    counter = 0 

    for i in minList:
        if int(i) == minMonth:    
            print(dateList[counter] + " " + str(minMonth))
            break 
        counter +=1

    #for i in maxList:
    ##    if maxMonth == int(i):
    #        print((dateList[i]))
    #for _ in minList:
    #    if minMonth == int(_['Profit/Losses']):
    #        print('dateList'[_])

 
    #findDataCount(bank_data)
    #findPLTotal(bank_data)

    