import pytest
from calcul import Calculation

@pytest.mark.calcul
def test_sum():
    calc = Calculation()
    assert calc.sum(2, 3) == 5

@pytest.mark.calcul
def test_sub():
    calc = Calculation()
    assert calc.sub(5, 3) == 2

@pytest.mark.calcul
def test_multiply():
    calc = Calculation()
    assert calc.multiply(2, 3) == 6

@pytest.mark.calcul
def test_div():
    calc = Calculation()
    assert calc.div(6, 3) == 2

@pytest.mark.skip(reason="Пересмотри пример")
def test_invisible():
    assert 33 == 5