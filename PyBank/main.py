import csv
import os

csvpath_bank = os.path.join('..', 'UTAUS201810DATA2', 'Python', 
                        'Homework', 'Instructions', 'PyBank', 
                        'Resources', 'budget_data.csv')

with open(csvpath_bank, newline='') as csvfile_bank:
    csvreader_bank = csv.reader(csvfile_bank, delimiter=',')

    csv_header_bank = next(csvfile_bank)
    print(f"Header: {csv_header_bank}")

    for row in csvreader_bank:
        print(row)

