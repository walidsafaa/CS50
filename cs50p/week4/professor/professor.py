import random


def main():
    generate_integer(get_level())


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    count = 0
    score = 0
    while count < 10:
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        q = x + y

        counter = 3
        while counter > 0:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == q:
                    score += 1
                    break
                else:
                    print("EEE")
                counter -= 1

            except ValueError:
                counter -= 1
                print("EEE")

        # solution
        if counter == 0:
            print(f"{x} + {y} = {q}")

        count += 1

    return print(f"Score: {score}")


if __name__ == "__main__":
    main()
