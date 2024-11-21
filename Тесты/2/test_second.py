import pytest
from main import Palindrom

@pytest.fixture
def prov():
    return Palindrom()

def test_palindrome(prov):
    assert prov.find_palindrome("тест") == False
    assert prov.find_palindrome("ку") == False
    assert prov.find_palindrome("Лёша на полке клопа нашёл") == True

def test_palindrome1(prov):
    assert prov.find_palindrome("Привет") == False
    assert prov.find_palindrome("Люди") == False
    assert prov.find_palindrome("") == False