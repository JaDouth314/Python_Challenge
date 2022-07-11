#Dependencies
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
Month_Total = []
Net_Total = []
Net_Change = []



#Open the CSV file
with open(csvpath) as csvfile:
    csvreader =  csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    #for row in csvreader:
       # print(row)
    
#Determine number of months
    for row in csvreader:
        Month_Total == 0
        Month_Total.append(row[0])    
#Determine net total amount of entire dataset
        Net_Total == 0
        Net_Total.append(int(row[1]))

#Loop through the profits to get average change
    for x in range(len(Net_Total)-1):
        Net_Change.append(Net_Total[x+1] - Net_Total[x])
        # Net_Change = Net_Total / Month_Total

#Determine the max increase and decrease values
    Max_Increase_Ammount = max(Net_Change)
    Max_Decrease_Ammount = min(Net_Change)
#Search the index of all the net change values and pull the corresponding date
    Max_Month_Increase = Net_Change.index(max(Net_Change))
    Max_Month_Decrease = Net_Change.index(min(Net_Change))

 #Print outcomes       
    print(f"The number of months is: ", len(Month_Total))   
    print(f"The sum total for the set is: $", sum(Net_Total))
    print(f"Average change of the profits/losses is: $", (round(sum(Net_Change)/len(Month_Total), 2)))
    print(f"Greatest profit increase happened in: {Month_Total[Max_Month_Increase]} with a value of ${str(Max_Increase_Ammount)}")
    print(f"Greatest profit decrease happened in: {Month_Total[Max_Month_Decrease]} with a value of ${str(Max_Decrease_Ammount)}")
    

#Print to a new CSV file
output_path = os.path.join('Analysis', "PyBank_Analysis")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvfile.write(f"The number of months is:  {len(Month_Total)}")
    csvfile.write("\n")
    csvfile.write(f"The total amount is: {sum(Net_Total)}")
    csvfile.write("\n")
    csvfile.write(f"The average change is:  {str(round(sum(Net_Change)/len(Month_Total), 2))}")
    csvfile.write("\n")
    csvfile.write(f"The greatest increase in profits was in: {Month_Total[Max_Month_Increase]} at ${str(Max_Increase_Ammount)}")
    csvfile.write("\n")
    csvfile.write(f"The greatest increase in profits was in: {Month_Total[Max_Month_Decrease]} at ${str(Max_Decrease_Ammount)}")