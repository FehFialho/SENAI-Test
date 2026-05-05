import sys
import os

# Adiciona o diretório pai (Start) ao sys.path para poder importar Calculator
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Conversor import fahToCels, celsToFah

def test_fahToCels():
    assert fahToCels(32) == 0

def test_fahToCels():
    assert celsToFah(0) == 32