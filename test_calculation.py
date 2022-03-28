import calculation

def test_square():
    a=10
    result=calculation.square(a)
    assert result == a*a

def test_perimeter():
    l=20
    w=10
    result=calculation.perimeter(l,w)
    assert result == 2*(l+w)

def test_area():
    l=20
    w=10
    result=calculation.area(l*w)
    assert result == l*w