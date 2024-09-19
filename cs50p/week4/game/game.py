import random

while True:
    try:
        n = int(input('Level: '))
        answer = random.randint(1, n)
        while True:
                guess = int(input('Guess: '))

                if guess > answer:
                    print("Too large!")
                elif guess < answer:
                    print("Too small!")
                else:
                    print("Just right!")
                    raise EOFError
    except ValueError:
        pass
    except EOFError:
        break

