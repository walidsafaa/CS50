from jar import Jar
import pytest

jar = Jar()


def main():
    test_init()
    test_deposit()
    test_withdraw()
    test_str()


def test_init():
    jar = Jar()


def test_deposit():
    jar.deposit(2)


def test_withdraw():
    jar.withdraw(1)


def test_str():
    assert str(jar) == "🍪"


if __name__ == "__main__":
    main()
