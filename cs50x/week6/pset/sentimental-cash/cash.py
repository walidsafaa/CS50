# TODO
import cs50


def main():
    change = positive()
    s = float_converter(change)

    quarters = 25.0
    dimes = 10.0
    nickels = 5.0
    pennies = 1.0

    count = 0
    while s >= quarters:
        count += 1
        s = s - quarters

    while s >= dimes:
        count += 1
        s = s - dimes

    while s >= nickels:
        count += 1
        s = s - nickels

    while s >= pennies:
        count += 1
        s = s - pennies

    print(f"{count}")


def positive():
    while True:
        try:
            n = float(input("Change owed: "))
            if n > 0:
                return n
        except ValueError:
            print("Not a positive num")


def float_converter(n):
    s = str(n)
    a = len(s) - 2
    b = (n % 10) / 10
    x = str(b)
    if n < 1.0:
        d = n * (10**a)
        return d
    elif len(x) > 4:
        d = n * (10**a) * 10
        return d
    else:
        return n * 100


main()
