# Saves names and numbers to a CSV file

import csv

# Get name and number
name = input("Name: ")
number = input("Number: ")
word = ""
# Open CSV file
file = open("phonebook.csv", "r")

for line in file:
    word = line.rstrip()
    word.add(word)

if name in file:
    # Print to file
    writer = csv.writer(file)
    writer.writerow([name, number])
