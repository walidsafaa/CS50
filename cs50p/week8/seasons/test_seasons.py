from seasons import Convert
import pytest

def main():
    test_convert()

def test_convert():
    assert Convert.minutes("2000-01-01") == "Twelve million, five hundred twenty-two thousand, two hundred forty minutes"
    assert Convert.minutes("2003-01-01") == "Ten million, nine hundred forty-four thousand minutes"
    assert Convert.minutes("2032-01-01") == "Minus four million, three hundred eight thousand, four hundred eighty minutes"
    with pytest.raises(SystemExit):
        Convert.minutes("1 January 2023")


if __name__ == "main":
    main()