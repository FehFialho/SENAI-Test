import sys
import os

# Adiciona o diretório pai (Start) ao sys.path para poder importar Calculator
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Calculator import sum, subtract, multiply, divide

def test_sum():
    assert sum(1, 2) == 3

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(5, 0) is None