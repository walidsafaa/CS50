import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Error: command line usage")
    database = []
    # TODO: Read database file into a variable
    # datafile = open(sys.argv[1], "r")
    check = 0
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for name in reader:
            if len(name) > 8:
                name["TTTTTTCT"] = int(name["TTTTTTCT"])
                name["TCTAG"] = int(name["TCTAG"])
                name["GATA"] = int(name["GATA"])
                name["AATG"] = int(name["AATG"])
                name["TATC"] = int(name["TATC"])
                name["GAAA"] = int(name["GAAA"])
                name["TCTG"] = int(name["TCTG"])
                name["AGATC"] = int(name["AGATC"])
                check += 1
            else:
                name["AGATC"] = int(name["AGATC"])
                name["AATG"] = int(name["AATG"])
                name["TATC"] = int(name["TATC"])
            database.append(name)
    # TODO: Read DNA sequence file into a variable
    seq_file = open(sys.argv[2], "r")
    sequence = seq_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    if check > 0:
        AGATC = longest_match(sequence, "AGATC")
        TTTTTTCT = longest_match(sequence, "TTTTTTCT")
        TCTAG = longest_match(sequence, "TCTAG")
        AATG = longest_match(sequence, "AATG")
        GATA = longest_match(sequence, "GATA")
        TATC = longest_match(sequence, "TATC")
        GAAA = longest_match(sequence, "GAAA")
        TCTG = longest_match(sequence, "TCTG")
    else:
        AATG = longest_match(sequence, "AATG")
        AGATC = longest_match(sequence, "AGATC")
        TATC = longest_match(sequence, "TATC")

    # TODO: Check database for matching profiles

    if check > 0:
        for i in range(len(database)):
            count = 0
            if database[i]["AGATC"] == AGATC:
                count += 1
            if database[i]["TTTTTTCT"] == TTTTTTCT:
                count += 1
            if database[i]["AATG"] == AATG:
                count += 1
            if database[i]["TCTAG"] == TCTAG:
                count += 1
            if database[i]["GATA"] == GATA:
                count += 1
            if database[i]["TATC"] == TATC:
                count += 1
            if database[i]["GAAA"] == GAAA:
                count += 1
            if database[i]["TCTG"] == TCTG:
                count += 1
            if count == 8:
                print(f"{database[i]['name']}")
                break
            if i == (len(database) - 1):
                print("No match")
    else:
        for i in range(len(database)):
            count = 0
            if database[i]["AGATC"] == AGATC:
                count += 1
            if database[i]["AATG"] == AATG:
                count += 1
            if database[i]["TATC"] == TATC:
                count += 1
            if count == 3:
                print(f"{database[i]['name']}")
                break
            if i == (len(database) - 1):
                print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
