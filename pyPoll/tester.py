import csv
from collections import Counter

with open('election_data2.csv', 'r') as csvfile:
    poll_data = csv.DictReader(csvfile, delimiter=',')

    names = ['Li', 'Correy','Khan', "O'Tooley"]
        
    candidates = []

    for row in poll_data:  
        candidates.append(row['Candidate'])

    count_candidates = Counter(candidates)

    print(count_candidates)




    #c = collections.Counter()
    
    #print(c)
    #print(Counter)

    #'percentages = set(names).intersection(poll_data['Candidates'])
    # 
    # print(percentages)
    
    #for name in names:
     #   for row in poll_data:
      #      candidateCount += 1
       #     print('Name: ' + name)
        #    print('Candidate: ' + row['Candidate'])    
         #   print(candidateCount)
            
            #if name == row['Candidate']:
             #   candidateCount += 1
      #  percentages.update({name: candidateCount})        
       # print(percentages)
       # candidateCount = 0


#def determine_percentages(csv_file, names, votes, totals):#
 #   with open(csv_file, 'r') as csvfile:
  #      poll_data = csv.DictReader(csvfile, delimiter=',')

 #       percentages = {}
  #      candidateCount = 0

   #     names = ['Li', 'Correy','Khan', "O'Tooley"]

   #    for name in names:
    #        for row in poll_data:
  #              if name == row['Candidate']:        
    #                candidateCount += 1
     #       percentages.update({name: candidateCount})        
      #      candidateCount = 0    
    
  #  return percentages       
    


def determine_percentages(csv_file, votes, totals):
    
    percentages = totals

    percentages.update({n: 2*(percentages[n]/votes) for n in percentages.keys()})       
       
    return percentages