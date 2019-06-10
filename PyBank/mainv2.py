import os
import csv

#col = []
#total_months = 0
#total_profitlosses = 0
#total_of_differences = int
#total_avg_difference = 0
#x_totaldifferences = 0
#x_length = 0
#average_change = 0
#greatest_increase = 0
#greatest_decrease = 0


#average_change = 0
#greatest_increase = 0
#greatest_decrease = 0

#csvpath = os.path.join("budget_data1.csv")
#csv = "budget_data1.csv"
#csvfile = open(csvpath)
#next(csvfile)
#data = csv.read()

total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0

with open("budget_data1.csv") as revenue_data:
   reader = csv.DictReader(revenue_data)

   for row in reader:

#csvpath = os.path.join("budget_data1.csv")
#csvfile = open(csvpath)
#next(csvfile)
#data = csvfile.read()

#with open(csvpath, newline='') as csvfile:
#    csvreader = csv.reader(csvfile, delimiter=',')
#    print(csvreader)
#    csv_header = next(csvreader)
#   print(f"CSV Header: {csv_header}")
#   for row in csvreader:
#      print(row)


        # Track the total
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["ProfitLosses"])

        # Track the revenue change
        revenue_change = int(row["ProfitLosses"]) - prev_revenue
        prev_revenue = int(row["ProfitLosses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        # Calculate the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        # Calculate the greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# Calculate the Average Revenue Change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)