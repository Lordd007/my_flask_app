import unittest
from ..calculator import Calculator

def test_add():
    assert Calculator().add(2, 3) == 5

def test_subtract():
    assert Calculator().subtract(7, 4) == 3
