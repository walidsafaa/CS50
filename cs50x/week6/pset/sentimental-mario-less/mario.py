# TODO


def main():
    height = get_height()
    for i in range(height):
        for x in range(height):
            a = x + i
            if a >= height - 1:
                print("#", end="")
                a -= 1
            else:
                print(" ", end="")

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
