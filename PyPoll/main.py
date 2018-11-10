

import os
import csv
import operator

csvpath_poll = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath_poll, newline='') as csvfile_poll:
    csvreader_poll = csv.reader(csvfile_poll, delimiter=',')


    csvheader_poll = next(csvfile_poll)
    print(f"Header: {csvheader_poll}")

    total_votes = 0
    tally_1 = 0
    tally_2 = 0
    tally_3 = 0
    tally_4 = 0
    candidate_names = []
    results = {}

    for row in csvreader_poll:

        total_votes += 1

        if row[2] not in candidate_names:
            candidate_names.append(row[2])
    

        if candidate_names[0] == row[2]:
            tally_1 += 1
        elif candidate_names[1] ==row[2]:
            tally_2 += 1
        elif candidate_names[2] == row[2]:
            tally_3 += 1
        else:
            tally_4 += 1


    print(tally_1)
    print(tally_2)
    print(tally_3)
    print(tally_4) 

    list_tallies = [tally_1, tally_2, tally_3, tally_4]

    final_results = dict(zip(candidate_names, list_tallies))
    print(final_results)
    winner = max(final_results.items(), key=operator.itemgetter(1))[0]   
        
    percent_1 = round(tally_1/total_votes * 100, 3)
    percent_2 = round(tally_2/total_votes * 100, 3)
    percent_3 = round(tally_3/total_votes * 100, 3)
    percent_4 = round(tally_4/total_votes * 100, 3)





print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidate_names[0]}: {percent_1}% ({tally_1})")
print(f"{candidate_names[1]}: {percent_2}% ({tally_2})")
print(f"{candidate_names[2]}: {percent_3}% ({tally_3})")
print(f"{candidate_names[3]}: {percent_4}% ({tally_4})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

output_path = os.path.join("election_results.csv")

with open(output_path, "w", newline='') as election_results:
    csvwriter = csv.writer(election_results)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"{candidate_names[0]}: {percent_1}% ({tally_1})"])
    csvwriter.writerow([f"{candidate_names[1]}: {percent_2}% ({tally_2})"])
    csvwriter.writerow([f"{candidate_names[2]}: {percent_3}% ({tally_3})"])
    csvwriter.writerow([f"{candidate_names[3]}: {percent_4}% ({tally_4})"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------------"])
