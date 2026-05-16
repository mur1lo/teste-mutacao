import pytest
from rh import calcular_bonus

def test_desenvolvedor_com_mais_de_dois_anos():
    assert calcular_bonus(3, 'DESENVOLVEDOR', 4000) == 600.0

def test_desenvolvedor_com_exatamente_dois_anos():
    assert calcular_bonus(2, 'DESENVOLVEDOR', 4000) == 0

def test_desenvolvedor_com_menos_de_dois_anos():
    assert calcular_bonus(1, 'DESENVOLVEDOR', 4000) == 0

def test_outro_cargo_com_mais_de_dois_anos():
    assert calcular_bonus(4, 'GERENTE', 4000) == 0