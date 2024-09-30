import pytest

from src.top import Top
from src.card import Card

def test_init():
    t1 = Top(Card.load(5))
    t2 = Top(Card.load(9), score = 9)
    
    assert t1.card == Card(5)
    assert t1.score == 0
    assert t2.card == Card(9)
    assert t2.score == 9
    

def test_repr():
    t1 = Top(Card.load(4))
    t2 = Top(Card.load(15), score = 2)
    
    assert t1.__repr__() == '|4| score: 0'
    assert t2.__repr__() == '|15| score: 2'
    

def test_save():
    t1 = Top(Card.load(7))
    t2 = Top(Card.load(23), score = 22)
    
    assert t1.save() == {'card': 7, 'score': 0}
    assert t2.save() == {'card': 23, 'score': 22}
    
    
def test_load():
    d1 = {'card': 8, 'score': 0}
    d2 = {'card': 23, 'score': 22}
    
    assert Top.load(d1) == Top(Card.load(8))
    assert Top.load(d2) == Top(Card(23), 22)