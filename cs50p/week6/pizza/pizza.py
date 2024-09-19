import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")


try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        headers = reader.fieldnames
        table = {name: [] for name in reader.fieldnames}
        for row in reader:
            for name in reader.fieldnames:
                table[name].append(row[name])

except FileNotFoundError:
    sys.exit("File does not exist")

print(table)
print(tabulate(table, headers, tablefmt="grid"))
