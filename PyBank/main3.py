import os
import csv

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