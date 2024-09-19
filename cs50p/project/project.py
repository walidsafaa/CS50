from tabulate import tabulate
from datetime import datetime
import re
import csv
import sys


def main():
    table = [
        {
            "Title": "Title",
            "Register Time": "Register Time",
            "Reminder Time": "Reminder Time",
            "Discription": "Discription",
        }
    ]
    task(table)


def task(table):
    while True:
        try:
            print("Create a new task.")
            while True:
                try:
                    title = input("Title: ")
                    if not title:
                        raise ValueError("Title cannot be empty")
                    else:
                        while True:
                            try:
                                discription = input("Discription: ")
                                if not discription:
                                    raise ValueError("Description cannot be empty")
                                else:
                                    break
                            except ValueError:
                                pass
                        break
                except ValueError:
                    pass
            reminder = time()
            table.append(
                {
                    "Title": title,
                    "Register Time": reminder[0],
                    "Reminder Time": reminder[1],
                    "Discription": discription,
                }
            )
            ftable(table)
            print("To exit the program and save the tasks, press Ctrl+D for macOS/Linux or Ctrl+Z for Win.")
        except EOFError:
            # Save the spereadsheet
            with open("Saved_Tasks.csv", "w") as output:
                writer = csv.DictWriter(output, fieldnames=table[0])
                for row in table:
                    writer.writerow(row)
                check_output(0)
            print()
            print("Tasks saved. Exiting the program.")
            sys.exit(0)



def time():
    while True:
        try:
            print(
                "TIME FORMAT: day-month-year //optional: (24-hours time) !All numbers must be 2-digits like 01 not 1"
            )
            reminder = input("Reminder time: ")
            if matches := re.search(
                r"^(\d+)-(\d+)-(\d+) ?(\d+)?:?(\d+)?$", reminder, re.IGNORECASE
            ):
                if matches.group(4) != None:
                    reminder = datetime.strptime(reminder, "%d-%m-%y %H:%M")
                    break
                else:
                    reminder = datetime.strptime(reminder, "%d-%m-%y")
                    break
        except ValueError:
            pass

    now = datetime.now()
    return (now.strftime("%d %b %Y %H:%M"), reminder.strftime("%d %b %Y %H:%M"))


def ftable(table):
    print(tabulate(table[1:], table[0], tablefmt="grid"))

def check_output(n):
    if n == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
