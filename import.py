import csv
with open('insurance.csv', newline='') as csvfile:
    reader =csv.DictReader(csvfile)
    for row in reader:
        print(row)