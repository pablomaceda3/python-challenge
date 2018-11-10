
#Import csv and os modules for additional functionality.

import csv
import os

# Path to relevant data file. 
csvpath_bank = os.path.join('..', 'Resources', 'budget_data.csv')

# Open csv file and set to read. Delimiter is ',' because
# they're comma-separated values.
with open(csvpath_bank, newline='') as csvfile_bank:
    csvreader_bank = csv.reader(csvfile_bank, delimiter=',')

    # Has header. `next()` is a function that skips a row
    # for an iterable. 
    csv_header_bank = next(csvfile_bank)
    print(f"Header: {csv_header_bank}")


    # Initialize variables used in for loop. 
    # Names should describe what variables hold. 
    count_row_months = 0
    net_profits_losses = 0
    agg_bw_months = 0
    avg_bw_months = 0
    prev_month = 0 
    agg_bw_months_check = 0
    greatest_decrease = 0
    greatest_increase = 0

    # `for` loop iterates through rows
    for row in csvreader_bank:
        count_row_months += 1
        
        profits_losses = int(row[1])
        net_profits_losses += profits_losses

        curr_month = row[1]
        change_bw_months = int(curr_month) - int(prev_month)
        avg_bw_months = (change_bw_months)/2

        agg_bw_months += avg_bw_months
        prev_month = curr_month

        if greatest_decrease > change_bw_months:
            greatest_decrease = change_bw_months
            greatest_decrease_date = row[0]
        elif greatest_increase < change_bw_months:
            greatest_increase = change_bw_months
            greatest_increase_date = row[0]



print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count_row_months}")
print(f"Total Net Profits/Losses: ${net_profits_losses}")
print(f"Average Change Between Months: ${agg_bw_months}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

output_path = os.path.join("financial_analysis.csv")

with open(output_path, "w", newline='') as financial_analysis:
    csvwriter = csv.writer(financial_analysis)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {count_row_months}"])
    csvwriter.writerow([f"Total Net Profits/Losses: ${net_profits_losses}"])
    csvwriter.writerow([f"Average Change Between Months: ${agg_bw_months}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"])



