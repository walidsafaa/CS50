def main():
    time = input("What time is it? ").strip()

    time = convert(time)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")


def convert(time):
    time = time.split(":")
    time12 = time[1].split(" ")

    if len(time12) > 1:
        if time12[1] == "a.m." or time12[1] == "am":
            if float(time[0]) == 12:
                return (float(time[0]) - 12) + float(time12[0]) / 60
            else:
                return float(time[0]) + float(time12[0]) / 60
        elif time12[1] == "p.m." or time12[1] == "pm":
            if float(time[0]) == 12:
                return float(time[0]) + float(time12[0]) / 60
            else:
                return (float(time[0]) + 12) + float(time12[0]) / 60
    else:
        return float(time[0]) + float(time[1]) / 60


if __name__ == "__main__":
    main()
