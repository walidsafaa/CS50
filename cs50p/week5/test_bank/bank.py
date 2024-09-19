def main():
    greeting = input("Greeting: ")
    print(f'${value(greeting)}')

def value(greeting):
    greeting = greeting.strip().lower()

    if 'hello' in greeting:
        return 0

    for word in greeting.split(' '):
        if word[0] == 'h':
            return 20

    return 100


if __name__ == "__main__":
    main()