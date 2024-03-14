# Dependancies 
import csv
import re

# files to load and output 
file_to_load = "/Users/archanakale/Documents/GitHub/Python-challenge-/PyBank/Resources/budget_data.csv"
file_to_output = "/Users/archanakale/Documents/GitHub/Python-challenge-/PyBank/Analysis/output.txt"

# Initialize variables
total_months = 0
total_revenue = 0
revenue_change = 0
revenue_change_list = []
month_of_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_months_list = []
total_revenue_list = []


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:

        # Track the total
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        # Track the revenue change
        if total_months == 1:
            revenue_change = int(row["Profit/Losses"])
        else:
            revenue_change = int(row["Profit/Losses"]) - revenue_change
            revenue_change_list = revenue_change_list + [revenue_change]
            month_of_change = month_of_change + [row["Date"]]
            revenue_change = int(row["Profit/Losses"])

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
    # Print Results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_revenue}")
    print(f"Average Change: ${revenue_avg}")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
    
    # Export a text file with the results
    with open(file_to_output, "w") as txt_file:
        txt_file.write("Financial Analysis\n")
        txt_file.write("----------------------------\n")
        txt_file.write(f"Total Months: {total_months}\n")
        txt_file.write(f"Total: ${total_revenue}\n")
        txt_file.write(f"Average Change: ${revenue_avg}\n")
        txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
        txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")