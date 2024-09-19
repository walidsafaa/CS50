from project import time, ftable, check_output
import pytest
from unittest.mock import patch


def main():
    test_check_output()
    test_time()
    test_ftable()

def test_check_output():
    assert check_output(0) == True
    assert check_output(1) == False
    assert check_output(50) == False

def test_time():
    with patch('builtins.input', return_value="01-01-23 12:30"):
        result = time()
        expected = ('25 Oct 2023 12:15', '01 Jan 2023 12:30')
        assert result == expected

def test_ftable():
    ftable("Date") == "Date"