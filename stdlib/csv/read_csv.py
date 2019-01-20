import csv

csvfile = 'SH600300_60.csv'
with open(csvfile, 'r', newline='') as fh:
    reader = csv.reader(fh)
    for row in reader:
        print(row)