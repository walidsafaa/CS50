from bank import value


def main():
    test_greeting()


def test_greeting():
    assert value("hello") == 0
    assert value("Hi!") == 20
    assert value("What's up") == 100



if __name__ == "__main__":
    main()
