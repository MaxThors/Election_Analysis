# The data we need to retrieve.

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() funciton with the "w" mode we will write data to the file
open(file_to_save, "w")

# 1. Initialize the total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and red the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        # 2. Add tot the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Print the candidate vote dictionary
print(candidate_votes) 

# 1. The total number of votes cast
# 2. A complete list of candidates who received votese
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the eledtion based on the popular vote.