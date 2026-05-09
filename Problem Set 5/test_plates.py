import pytest
from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCD232") == False
    assert is_valid("BC23") == True

def test_first_char():
    assert is_valid("AB22") == True
    assert is_valid("22AB") == False

def test_number():
    assert is_valid("123AB") == False
    assert is_valid("ABC12") == True
    assert is_valid("AB2C") == False

def test_zero():
    assert is_valid("ABC02") == False
    assert is_valid("ABC20") == True

def test_letters():
    assert is_valid("AD@24") == False
    assert is_valid("AD,23") == False