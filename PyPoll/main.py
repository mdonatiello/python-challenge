# Dependencies
import csv

# Files to load and output (Remember to change these)
file_to_load = "election_data.csv"
file_to_output = "electionresults.txt"

# Track various election parameters
total_votes_cast = 0
candidates = []
candidates_votes = {}
election_winner_popvote = ""
election_winner_count = 0

with open(file_to_load) as data:
    reader = csv.DictReader(data)

# Determine th winner by looping through counts:
    for row in reader:
        # Retrieve vote count and percentage:
        total_votes_cast = total_votes_cast + 1
        candidate_name = row["Candidate"]
            
#Determine winning vote count and candidate:
        if candidate_name not in candidates:
           candidates.append(candidate_name)
           candidates_votes[candidate_name] = 0
        candidates_votes[candidate_name] = candidates_votes[candidate_name] + 1

with open(file_to_output, "w") as txt_file:
    totalvotes_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes_cast}\n"
        f"-------------------------\n")
    print(totalvotes_results, end="")
    txt_file.write(totalvotes_results)

    for Candidate in candidates_votes:
        votes = candidates_votes.get(Candidate)
        percentage_of_votes_won = float(votes)/float(total_votes_cast) * 100

        if(votes > election_winner_count):
            election_winner_count = votes
            election_winner_popvote = Candidate

        votes_output = f"{Candidate}: {percentage_of_votes_won:.3f}% ({votes})\n"
        print(votes_output, end="")
        txt_file.write(votes_output)

    election_winner_summary = (
        f"-------------------------\n"
        f"Winner: {election_winner_popvote}\n"
        f"-------------------------\n")
    print(election_winner_summary)
    txt_file.write(election_winner_summary)
