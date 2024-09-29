import pytest
from src.card import Card


def test_init():
    c = Card(12)
    c1 = Card(12.0)
    assert c.value == 12
    assert c1.value == 12


def test_repr():
    c = Card(12)
    assert c.__repr__() == '|12|'
    assert Card.__repr__(Card(13)) == '|13|'


def test_validation():
    with pytest.raises(ValueError):
        Card(1)
    with pytest.raises(ValueError):
        Card('f')
    with pytest.raises(ValueError):
        Card('1')
    with pytest.raises(ValueError):
        Card(-1)
    with pytest.raises(ValueError):
        Card('25')
    with pytest.raises(ValueError):
        Card(100)
    with pytest.raises(ValueError):
        Card(3.5)
    with pytest.raises(ValueError):
        Card('6.7')
    with pytest.raises(ValueError):
        Card(-5)
        

def test_eq():
    a = Card(7)
    c = Card(12)
    b = Card(12.0)
    d = Card(12)
    
    assert c == b
    assert c == d
    assert c == Card(12) 
    assert c != a
    assert c != Card(10)


def test_save():
    c = Card(15)
    b = Card(4).save()
    
    assert c.save() == 15
    assert b == 4
    
    
def test_load():
    a = Card(15)
    c = 15
    b = Card(15).save()
    
    assert Card.load(c) == a
    assert Card.load(b) == a
    assert Card.load(a.save()) == a
    assert Card.load(Card(15).save()) == a


def test_all_cards():
    a = Card.all_cards([val for val in range(3, 7)])
    b = Card.all_cards()
    
    assert a == [Card(3), Card(4), Card(5), Card(6)]
    assert b == [Card(val) for val in range(3, 36)]
    
    
    