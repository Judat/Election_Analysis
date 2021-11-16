# The Data we need to retreive
# 1.Total number of votes cast
# 2.A complete list of candidates who received votes
# 3.Total number of votes each candidate received
# 4.Percentage of votes each candidate won
# 5.The winner of the election based on popular vote
# import datetime
# now = datetime.datetime.now()
# print("The time right now is ", now)

# import datetime as dt
# now = dt.datetime.now()
# print("the time right now is " , now)
import csv
import os
# dir (csv)
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
  # Print each row in the CSV file.
   # for row in file_reader:
    #    print(row)
#print the header row
    headers = next(file_reader)
    print (headers)


    


