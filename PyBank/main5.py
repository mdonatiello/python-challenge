# Dependencies
import os
import csv

# Files to load
file_to_load = "budget_data1.csv"

# Track various revenue parameters
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:

        # Track the total
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["ProfitLosses"])

        # Track the revenue change
        revenue_change = int(row["ProfitLosses"]) - prev_revenue
        prev_revenue = int(row["ProfitLosses"])
 #      revenue_change_list = revenue_change_list + [revenue_change]
        revenue_change_list += [revenue_change]
        month_of_change = month_of_change + [row["Date"]]
	
#       print("Start Sample Print")
#       print("Revenue Change List :")
#       print(revenue_change_list)
#       print("Month of Change :") 
#       print(month_of_change)
#       print("End Sample Print")

        avg_revenue_change = revenue_change_list[i] / month_of_change

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

# Generate Output Summary
output = (
    f"Financial Analysis"
    f"-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${avg_revenue_change}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output
print(output)