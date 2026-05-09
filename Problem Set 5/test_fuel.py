import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("2/3") == 67
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_gauge():
    assert gauge(67) == "67%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"