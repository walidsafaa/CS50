def main():
    word = input('Word: ')
    print(shorten(word))

def shorten(word):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    for c in word:
        if c.upper() in vowels:
            word = word.replace(c, '')
    return f'{word}'

if __name__ == "__main__":
    main()