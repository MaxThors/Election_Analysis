# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent localcongressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes and which counties the votes came from.
3. Calculate the total number of votes each candidate received and how many came from each county.
4. Calculate the percentage of votes each candidate won and the percentage of votes that came from each county.
5. Determine the winner of the election based on the popular vote.

## Resources
- Data Source: election results.csv
- Software: Python 3.7.6, Visual Studio Code 1.52.1

## Election-Audit Results
The analysis of the electin show that:
- There were 369,711 votes cast in the election.
- The counties were:
  - Jefferson
  - Denver
  - Arapahoe
- The results were:
  - Jefferson County received 10.5% of the votes and 38,855 number of votes.
  - Denver County received 82.8% of the votes and 306,055 number of votes.
  - Arapahoe County received 6.7% of the votes and 24,801 number of votes.
- The county that received the most votes was:
  - Denver County, where 82.8% of the votes came from and 306,055 people voted.
-The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
  
## Challenge Summary
All in all, these script can be used for any elections with some simple modifications. This script provides quick results from a CSV file and
provides the results in a quick summary that is easy to read. However, one modification we could make is that we do not have to break it down 
into counties because not every election is broken down into counties. For example, it could be cities, states, districts, etc. Another modification
is that we could add even more breakdowns to do deeper analysis. If we had more information, two more examples of what we could break it down into 
polling location or time of day. Both of these are just two modifications that would not be difficult to add to the script since we already have 
a breakdown to do the coding since adding the counties was very similar to the candidate votes.
 
