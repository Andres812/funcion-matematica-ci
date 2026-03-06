import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from potencia import potencia


# Caso correcto
def test_potencia_correcta():
    assert potencia(2, 3) == 8


# Caso límite
def test_potencia_cero():
    assert potencia(5, 0) == 1


# Caso error
def test_error_tipo():
    with pytest.raises(TypeError):
        potencia("hola", 2)