
from unittest.mock import patch

# Evita iniciar o menu interativo durante a importação.
with patch("builtins.input", return_value="0"):
    from Calculadora import fatorial


def test_fatorial_de_zero_retorna_um():
    assert fatorial(0) == 1


def test_fatorial_de_um_retorna_um():
    assert fatorial(1) == 1


def test_fatorial_de_cinco_retorna_120():
    assert fatorial(5) == 120


def test_fatorial_de_seis_retorna_720():
    assert fatorial(6) == 720
