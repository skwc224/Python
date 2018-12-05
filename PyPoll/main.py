import os
import csv

electionCSV = os.path.join('..', 'Resources', 'election_data.csv')
output_file = os.path.join('election_analysis.txt')

totalVotes = 0
candidateVotes = {}

with open(electionCSV) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    
    for row in reader:
      
      totalVotes += 1
      name = row[2]
      
      if name not in candidateVotes:
        candidateVotes[name] = 1
      else:
        candidateVotes[name] += 1

with open(output_file, 'w') as textfile:

  election_results_1 = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {totalVotes}\n"
    f"-------------------------\n")
  print(election_results_1)
  writer = textfile.write(election_results_1)

  for candidate in candidateVotes:
    votePercentage = float(candidateVotes[candidate]) / float(totalVotes) * 100
    winner = max(candidateVotes, key = lambda k: candidateVotes[k])

    election_results_2 = (
      f"{candidate}: {votePercentage:.3f}% ({candidateVotes[candidate]})\n")
    print(election_results_2)
    writer = textfile.write(election_results_2)

    election_results_3 = (
      f"-------------------------\n"
      f"Winner: {winner}\n"
      f"-------------------------\n")
  print(election_results_3)
  writer = textfile.write(election_results_3)
