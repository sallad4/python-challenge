import csv
from collections import Counter
#product of dally g
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

def countVoters(csv_file):
    with open(csv_file, 'r') as csvfile:
        poll_data = csv.DictReader(csvfile, delimiter=',')

        count = 0

        for _ in poll_data: 
            count += 1
    
        return count

def candidate_list(csv_file):
    with open(csv_file, 'r') as csvfile:
        poll_data = csv.DictReader(csvfile, delimiter=',')

        candidates = []

        for row in poll_data:
           candidates.append(row['Candidate'])
        
        unique_candidates = set(candidates)
    
        return unique_candidates

def determine_vote_count(csv_file):
    with open(csv_file, 'r') as csvfile:
        poll_data = csv.DictReader(csvfile, delimiter=',')
        
        candidates = []

        for row in poll_data:  
            candidates.append(row['Candidate'])

        count_candidates = Counter(candidates)

        return count_candidates

def determine_percentages(totals, tally):
    
    percentages = tally

    percentages.update({n: ((percentages[n]/totals)-percentages[n]) for n in percentages.keys()})       
   
    return percentages

def winner_winner(votes):
    winner = max(votes, key=votes.get)

    return winner

def main():

    csv_data = "election_data2.csv"

    #determine total number of votes cast
    total_vote_count = countVoters(csv_data)
    print(total_vote_count)

    #find the candidates receiving votes
    candidate_names = candidate_list(csv_data)
    print(candidate_names)

    #find number of votes received by each candidate
    cand_vote_tally = determine_vote_count(csv_data)
    print(cand_vote_tally)
    
    #find the percentage of votes received by each candidate
    percentages = determine_percentages(total_vote_count, cand_vote_tally)
    print(percentages)

    #find and print the winner
    winner = winner_winner(cand_vote_tally)
    print(winner)

main()
#with open('election_data.csv', 'r') as csvfile:
#    bank_data = csv.DictReader(csvfile, delimiter=",")

#    count = 0

#    for _ in bank_data:
#        count += 1

#    print(count)