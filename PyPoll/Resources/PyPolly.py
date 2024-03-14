# Dependancies 
import csv

# files to load and output 
file_to_load = "/Users/archanakale/Documents/GitHub/Python-challenge-/PyPoll/Resources/election_data.csv"
file_to_output = "/Users/archanakale/Documents/GitHub/Python-challenge-/PyPoll/Analysis/output.txt"

# Total Votar counter
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as (election_data):
    csv_reader = csv.DictReader(election_data)

    # For each row in the CSV file.
    for row in csv_reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row["Candidate"]

        # If the candidate does not match any existing candidate add it to
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes [candidate_name] + 1

# Save the results to our text file.
with open(file_to_output, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results)

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    for candidate in candidate_votes:

        # Retrieve vote count of a candidate.
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print out winnning candidate to the terminal.
        voter_output = (f"{candidate}: {vote_percentage:.3f}% ({votes:,})\n")

        #  Save the candidate results to our text file.
        txt_file.write(voter_output)

    # Print the winning candidate's (results to the terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
