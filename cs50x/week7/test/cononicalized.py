import csv

titles = set()

with open("small.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        titles.add(row['age'].strip().upper()) #canonicalized

for title in titles:
    if "OFFICE" in title:
        print('The Office')
        break
    else:
        print("Not found")