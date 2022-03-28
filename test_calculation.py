import calculation
import pytest


def test_area_square():
    side=3
    result=calculation.area_square(side)
    assert result == side * side

@pytest.mark.perimeterarearec
def test_perimeter_rect():
    l=5
    w=8
    result=calculation.perimeter_rect(l,w)
    assert result == 2*(l+w)

@pytest.mark.perimeterarearec
def test_area_rect():
    l=5
    b=6
    result=calculation.area_rect(l,b)
    assert result == l*b
