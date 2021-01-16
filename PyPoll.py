# The data we need to retrieve.

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() funciton with the "w" mode we will write data to the file
open(file_to_save, "w")

# Open the election results and red the file
with open(file_to_load) as election_data:

    # To do: Read and analysis the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# 1. The total number of votes cast
# 2. A complete list of candidates who received votese
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the eledtion based on the popular vote.