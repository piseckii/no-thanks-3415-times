import pytest
from src.card import Card


def test_init():
    c = Card(12)
    assert c.value == 12
def test_repr():
    c = Card(12)
    assert c.__repr__() == '|12|'
    assert Card.__repr__(Card(13)) == '|13|'
    