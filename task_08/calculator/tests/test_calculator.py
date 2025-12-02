import pytest
from src.calculator import calculate

def test_add():
    assert calculate("2+2") == 4

def test_subtract():
    assert calculate("10-5") == 5

def test_multiply():
    assert calculate("3*4") == 12

def test_divide():
    assert calculate("10/2") == 5

def test_invalid_expression():
    with pytest.raises(ValueError):
        calculate("2+")

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculate("10/0")
