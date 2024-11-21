import pytest
from pow import pow2, pow2_math, pow3_math, fibonacci

@pytest.mark.pow2
def test_pow2():
    assert pow2(3) == 9

@pytest.mark.pow2
def test_pow2_math():
    assert pow2_math(3) == 9

@pytest.mark.pow3
def test_pow3_math():
    assert pow3_math(2) == 8

@pytest.mark.pow3
def test_fibonacci():
    assert fibonacci(6) == 8 

@pytest.mark.xfail(reason="ошибка")
def test_notpow():
    assert pow2(2) == 5