import os
import csv
csv_path = os.path.join('..', 'Homework 3', 'PyPoll', 'Resources', 'election_data.csv')
csv_path2 = os.path.join('..', 'PyPoll', 'Resources', "Results.txt")

total_votes = 0 
candidates = []
candidate_totals = [0, 0, 0]
percentage = [0, 0, 0]
winner = None



with open (csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    

    
    for row in csvreader:
#The total number of votes cast
            total_votes += 1
            candidate = row[2]
        
#A complete list of candidates who received votes
            if candidate not in candidates:
                candidates.append(candidate) 

#The total number of votes each candidate won  
            if candidate == candidates[0]:
                candidate_totals[0] += 1
            elif candidate == candidates[1]:
                candidate_totals[1] += 1
            elif candidate == candidates[2]:
                candidate_totals[2] += 1

# the percentage of votes each candidate won    
            percentage[0] = (candidate_totals[0] / total_votes) * 100
            percentage[1] = (candidate_totals[1] / total_votes) * 100
            percentage[2] = (candidate_totals[2] / total_votes) * 100

# The winner of the election based on popular vote
            winner_index = candidate_totals.index(max(candidate_totals))
            winner = candidates[winner_index]


output = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total votes: {total_votes}\n"
    f"----------------------------\n"
    f"{candidates[0]}: {percentage[0]:.3f}% ({candidate_totals[0]})\n"
    f"{candidates[1]}: {percentage[1]:.3f}% ({candidate_totals[1]})\n"
    f"{candidates[2]}: {percentage[2]:.3f}% ({candidate_totals[2]})\n"
    f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------\n")
    

print(output)


with open(csv_path2, "w") as textfile:
    textfile.write(output)
