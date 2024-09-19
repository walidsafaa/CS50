from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75

def test_value_error():
    with pytest.raises(ValueError):
        convert("1.5/3")

def test_zero_error():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(35) == "35%"
    assert gauge(99) == "F"
