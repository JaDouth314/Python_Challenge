#Dependencies
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
VoteTotal = []




#Open the CSV file
with open(csvpath) as csvfile:
    csvreader =  csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # for row in csvreader:
    #     print(row)

    for row in (csvfile):
        VoteTotal == 0
        VoteTotal.append(row[0])
        
    print(len(VoteTotal))

    #Print to a new CSV file
output_path = os.path.join('Analysis', "PyPoll_Analysis")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvfile.write(f"Election Results")
    csvfile.write("\n")
    csvfile.write(f"----------------")
    csvfile.write("\n")
    csvfile.write(f"The total number of votes was: {len(VoteTotal)}")