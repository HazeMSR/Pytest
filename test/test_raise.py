import pytest
from src.functions import f


"""
    Usando la librería de pytest asegura
    si la función 'f' provoca una 'salida
    del sistema'. 
"""

def test_mytest():
    with pytest.raises(SystemExit):
        f()
