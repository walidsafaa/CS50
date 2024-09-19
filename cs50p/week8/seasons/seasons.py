from datetime import date
import inflect
import sys


class Convert:
    def __init__(self, birthdate):
        self.birthdate = birthdate

    @classmethod
    def minutes(cls, birthdate):
        try:
            start = date.fromisoformat(birthdate)
            today = date.fromisoformat(str(date.today()))
            difference = today - start
            minutes = difference.total_seconds() / 60
            return Convert.text(minutes)
        except ValueError:
            sys.exit("Invalid date")

    @classmethod
    def text(cls, minutes):
        p = inflect.engine()
        return f"{p.number_to_words(round(minutes), andword='').capitalize()} minutes"


def main():
    print(Convert.minutes(input("Date of Birth: ")))


if __name__ == "__main__":
    main()
