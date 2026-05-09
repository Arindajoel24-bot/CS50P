import pytest 
from twttr import shorten

def test_string():
    assert shorten("hello") == "hll"

def test_no_vowels():
    assert shorten("fly") == "fly"

def test_capital_letters():
    assert shorten("ARINDA") == "RND"

def test_all_vowels():
    assert shorten("ai") == ""

def test_numbers():
    assert shorten("2") == "2"