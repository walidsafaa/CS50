import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1], "r") as file:
        reader = file.readlines()
        count = 0
        for row in reader:
            row = row.lstrip()
            if not row.startswith("#") and len(row) != 0:
                count += 1

except FileNotFoundError:
    sys.exit("File does not exist")

print(count)
