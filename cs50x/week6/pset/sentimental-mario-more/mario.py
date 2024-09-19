# TODO


def main():
    height = get_height()
    for b in range(height):
        for x in range(height - b - 1):
            print(" ", end="")

        a = -1
        while a < b:
            print("#", end="")
            a += 1

        print("  ", end="")

        d = -1
        while d < b:
            print("#", end="")
            d += 1

        print()


def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0 and n <= 8:
                return n
        except ValueError:
            print("Not an integer.")


main()
