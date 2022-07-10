#Dependencies
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#Open the CSV file
with open(csvpath) as csvfile:
    csvreader =  csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)

#Print to a new CSV file
output_path = os.path.join('Analysis', "PyPoll_Analysis")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Ballot', " County", " Candidate"])
    csvwriter.writerow(['100', " Jefferson", " Me"])