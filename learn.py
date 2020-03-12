import csv
with open('training_data.csv') as f:
    reader = csv.reader(f, skipinitialspace=True)
    header = next(reader)
    a = [dict(zip(header, map(str, row))) for row in reader]

for x in a:
    print(x['carrier'])
