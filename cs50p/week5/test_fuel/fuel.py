def main():
    while True:
        try:
            fraction = input("Fraction: ")
            if convert(fraction) != ValueError and convert(fraction) != ZeroDivisionError:
                break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(convert(fraction)))

def convert(fraction):
    fraction = fraction.strip().split("/")
    while True:
        try:
            x = int(fraction[0])
            y = int(fraction[1])
            if x <= y:
                return round(x / y * 100)

        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError


def gauge(percentage):
    if 1 < percentage < 99:
        return f"{percentage}%"
    elif percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"

if __name__ == "__main__":
    main()