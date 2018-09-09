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

def merge_votes_percents(cand_perc):
    cand_keys = []
    cand_values_per = []

    cand_keys = list(cand_perc.keys())
    print(cand_keys)

    cand_values_per = list(cand_perc.values())
    print(cand_values_per) 

def merge_votes_tally(cand_tally):
    cand_values = []

    cand_values = list(cand_tally.values())
    return(cand_tally) 
    

def print_to_file(total_vote_count, cand_tally_format, winner, cand_vote_tally):
    #keep your own path references in mind
    with open("election_results.txt", "w") as text_file:
        
        cand_tally_format = Counter(cand_vote_tally)
        cand_tally_format.keys()
        
        print("Election Results")
        print("-------------------------------")
        print(f'Total Votes: {total_vote_count}')
        print("-------------------------------")
        for ckey, cvalue in cand_tally_format.items():
            print(ckey, "{0:.3f}%".format(round(cvalue,3))) 
        print("-------------------------------")
        print('Winner: ' + winner)
        print("-------------------------------")
        text_file.close()

def main():

    csv_data = "election_data.csv"

    #determine total number of votes cast
    total_vote_count = countVoters(csv_data)

    #find the candidates receiving votes
    candidate_names = candidate_list(csv_data)

    #find number of votes received by each candidate
    cand_vote_tally = determine_vote_count(csv_data)
    
    #find the percentage of votes received by each candidate
    percentages = determine_percentages(total_vote_count, cand_vote_tally)

    #find and print the winner
    winner = winner_winner(cand_vote_tally)
     
    cand_tally_format = Counter(cand_vote_tally)
    cand_tally_format.keys()
 
    print("Election Results")
    print("-------------------------------")
    print(f'Total Votes: {total_vote_count}')
    print("-------------------------------")
    for ckey, cvalue in cand_tally_format.items():
        print(ckey, "{0:.3f}%".format(round(cvalue*100,3))) 
    print("-------------------------------")
    print('Winner: ' + winner)
    print("-------------------------------")

    print_to_file(total_vote_count, cand_tally_format, winner, cand_vote_tally)

main()
