# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Create County Options List
county_options = []

# Create a dictionary to sum County results
county_votes = {}

# Create Candidate Options list 
candidate_options = []

# Create a dictionary to sum candidate results
candidate_votes = {}

# Track the winning county, vote count and percentage.
winning_ctycounty = ""
winning_ctycount = 0
winning_ctypercentage = 0

# Track the winning candidate, vote count and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1

        # Print the county name from each row
        county_name = row[1]

        # If the county does not match any existing county ...
        if county_name not in county_options:
            # Add it to the list of counties
            county_options.append(county_name)

            #Begin tracking that county's vote
            county_votes[county_name] = 0

        # Add a vote to that county's count
        county_votes[county_name] += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate ...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Define county and candidate output lists
county_percent=[]
candidate_percent=[]       

# Determine the percentage of votes in each county by looping through the counts.
for county in county_votes:

    #Retreive vote count in each county
    votescty = county_votes[county]

    #Calculate the percentage of votes
    votescty_percentage = float(votescty) / float(total_votes) * 100

    county_percent.append(f"{county} received {votescty_percentage:.1f}% or {votescty:,} votes")

    # Store the county name and % of votes to the dictionary for each county
    if (votescty > winning_ctycount) and (votescty_percentage > winning_ctypercentage):
        winning_ctycount = votescty
        winning_ctycounty = county
        winning_ctypercentage = votescty_percentage

# Determine the percentage of votes for each candidate by looping through the counts.
for candidate in candidate_votes:
    
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate]

    # Calculate the percentage of votes 
    vote_percentage = float(votes) / float(total_votes) * 100
    
    candidate_percent.append(f"{candidate} received {vote_percentage:.1f}% or {votes:,} votes")
    
    # Store the candidate name and percentage of votes to the dictionary for each candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate
        winning_percentage = vote_percentage


# Save the results to our text file.
with open("Election_analysis.txt", "w") as txt_file:    


    # Topline functions for print formating
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n"
        f"County Votes: \n")
        
    county_results = (
        f"--------------------------\n"
        f"Largest County Turnout: {winning_ctycounty}\n"
        f"--------------------------\n")



    # Print the final vote count to the terminal.
    election_results += ("\n".join(county_percent))+("\n")+("".join(county_results))+("\n".join(candidate_percent)+("\n"))
    print (election_results)

#Save the final vote to the text file.
    txt_file.write(election_results) 

    


winning_candidate_summary = (
    f"\n--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n")

print(winning_candidate_summary)

        
    