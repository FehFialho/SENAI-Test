import sys
import os

# Adiciona o diretório pai (Start) ao sys.path para poder importar Calculator
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Area import square, triangle, elipsis

def test_square():
    assert square(2, 2) == 4

def test_triangle():
    assert triangle(2, 5) == 5

def test_elipsis():
    assert elipsis(6,5) == 94.25