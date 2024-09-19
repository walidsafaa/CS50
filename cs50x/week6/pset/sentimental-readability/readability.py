# TODO


def main():
    text = input("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = letters / words * 100
    S = sentences / words * 100

    index = round(0.0588 * float(L) - 0.296 * float(S) - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def count_letters(text):
    count = 0
    for i in range(len(text)):
        if text[i].isalpha():
            count += 1
    return count


def count_words(text):
    if text:
        x = sum(1 for c in text if c in " \t\n")
        return x + 1
    """
    or
    text = re.split(r'\s',text)
    count = len(text)
    """


def count_sentences(text):
    if text:
        x = sum(1 for c in text if c in ".?!")
        return x


main()
