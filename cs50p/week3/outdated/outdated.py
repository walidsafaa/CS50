months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

while True:
    try:
        date = input("Date: ").strip()

        if date[0].isalpha():
            month_day, year = date.split(", ")
            month, day = month_day.split(" ")
            if month.capitalize() in months and 0 < int(day) <= 31:
                print(f"{year}-{int(months[month.capitalize()]):02}-{int(day):02}")
                break
        else:
            month, day, year = date.split("/")
            if 0 < int(month) <= 12 and 0 < int(day) <= 31:
                print(f"{year}-{int(month):02d}-{int(day):02d}")
                break
    except ValueError:
        pass
