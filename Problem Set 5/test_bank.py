import pytest
from bank import value

def test_hello():
    assert value("hello") == "$0"
    assert value("HELLO") == "$0"

def test_hey():
    assert value("hey") == "$20"
    assert value("how are you") == "$20"

def test_any_word():
    assert value("tsap") == "$100"
    assert value("") == "$100"