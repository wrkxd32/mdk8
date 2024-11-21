import pytest
from main import Text_Greeting

tg = Text_Greeting()

@pytest.mark.parametrize("name, expected", [
    ("Anton", "Меня зовут Anton"),
    ("Aboba", "Меня зовут Aboba"),
    ("", "")
])
def test_greeting(name, expected):
    assert tg.greeting(name) == expected

@pytest.mark.skip(reason="ошибка")
def test_empty():
    assert tg.empty_string("") == False
def test_register():
    assert tg.register_check("hello") == True
    assert tg.register_check("Hello") == False

@pytest.mark.parametrize("string, expected", [
    ("Короткое", True),
    ("Длинное", True),
    ("Длиннее десяти", False)
])
def test_long(string, expected):
    assert tg.long_check(string) == expected

@pytest.mark.parametrize("arg, expected", [
    (924, False),
    (16.91, False),
    ("Строка", True)
])
def test_type(arg, expected):
    assert tg.string_type(arg) == expected