import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            clean(sys.argv[1], sys.argv[2])


def clean(input, output):
    try:
        with open(input) as input:
            reader = csv.DictReader(input)
            with open(sys.argv[2], "w") as output:
                headers = ["first", "last", "house"]
                writer = csv.DictWriter(output, fieldnames=headers)
                writer.writeheader()
                for row in reader:
                    row["name"] = row["name"].strip()
                    second, first = row["name"].split(",")
                    writer.writerow({"first": first.strip(), 'last': second.strip(), "house": row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {input}")

if __name__ == "__main__":
    main()

