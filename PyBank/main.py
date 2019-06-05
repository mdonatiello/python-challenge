import os
import csv

#col = []
total_months = 0
total = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0

csvpath = os.path.join("budget_data1.csv")
csvfile = open(csvpath)
#next(csvfile)
data = csvfile.read()

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
       print(row)
#      int(len(col[0]))
#      total_months=int(len(col[0]))
#      total_months = sum(1 for (row[0]) in "budget_data1.csv")
#      total_months = sum(1 for row in csvreader)
       total_months = len(data.splitlines()) - 1
       print(total_months)
       total += float(row[1])
       print(total)
       average_change = total / total_months
       print(average_change)       
#      length = len(numbers(row[1]))
#      average_change = total / length
#      def average(numbers):
#          length = len(numbers)
#          total = 0.0
#          average_change = 0.0
#          for number in numbers:
#               total_profitloss += float(row[1])
#               total += number
#          return total / length
#          average_change = (total / length)
#      print(average_change)
#          return total_profitloss / length
#          print(average(float(row[1]))
#          average_change = total_profitloss / length
#          return average_change
#          average_change = (total_profitloss += number)
#          print(average_change)
#      average_change = total/86
#      print(average_change)

    print("Financial Analysis")
    print("---------------------------------")
    print("Total Months:",total_months)
    print("Total:",total)
    print("Average Change:",average_change)
#   print("Greatest Increase in Profits:",greatest_increase)
#   print("Greatest Decrease in Profits:",greatest_decrease)


        
#   file = "budget_data1.csv" 
#   file.seek(0)
#   row_count = sum(1 for row in "budget_data1.csv")
#   print(row_count)
#   profitlosses_nettotal = sum(int(B2:B87) in "budget_data1.csv")
#   profitlosses_nettotal = sum(int(2,2:87,2) in "budget_data1.csv")
#   for r in rows:
#        print sum([float(r['Colum1'])])
 

#    lastrow = Cells(Rows.Count,2).End(xlUp).Row
#    print(lastrow)
 
#total = 0
#    col =     
#   
#    for col in row[1]:
#            total += int(col)
#    print(total)

#print(row)

#with open("budget_data1.csv") as fin:
#   headerline = fin.next()
#   total = 0
#  for row in csv.reader(fin):
#    print(col)
#   for col in row[1]:
#     total += int(col)
# print(total)


# def printFinancialAnalysis():
#   print(f"Financial Analysis")
# def print---------------------------------():
#   print(f"---------------------------------")

#Total number of months included in the dataset
#data = list(reader)
#row_count = len(data) - 1
#total_months = row_count
#def printTotalMonths():
#   print(f"Total Months:")total_months

#or
#lastrow = Cells(Rows.Count,2).End(xlUp).Row



#To csv write:

# Specify the file to write to
#output_path = os.path.join("..", "output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    #csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    #csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])