import pytest

from src.card import Card
from src.hand import Hand


def test_init():
    cards = [Card(12), Card(15), Card(16)]

    d = Hand(cards)

    assert d.cards == cards


def test_repr():
    cards = [Card(12), Card(15), Card(16)]

    d = Hand(cards)
    d1 = Hand([Card(9)])

    assert d.__repr__() == "[|12|, |15|, |16|]"
    assert d1.__repr__() == "[|9|]"
    assert Hand([Card(4)]).__repr__() == "[|4|]"


def test_eq():
    cards = [Card(12), Card(15), Card(16)]

    d = Hand(cards)
    d1 = Hand(cards)
    d2 = Hand([Card(12), Card(15), Card(16)])
    d3 = Hand([Card(4), Card(5)])

    assert d == d1
    assert d == d2
    assert d != d3


def test_save():
    cards = [Card(12), Card(15), Card(16)]

    d = Hand(cards)

    assert d.save() == [12, 15, 16]
    assert Hand(cards).save() == [12, 15, 16]
    assert Hand([Card(3)]).save() == [3]


def test_load():
    cards = [Card(12), Card(15), Card(16)]

    d = Hand(cards).save()

    assert Hand.load(d) == Hand(cards)
    assert Hand.load([12]) == Hand([Card(12)])


def test_add_card():
    cards = [Card(14), Card(16)]

    h = Hand(cards)

    assert h.add_card(Card(15)).cards == [Card(14), Card(16), Card(15)]
    assert h == Hand([Card(14), Card(16), Card(15)])


def test_score():
    h1 = Hand.load([4, 8, 6, 9, 5])
    h2 = Hand([Card(card) for card in [4, 8, 6, 9, 5]])
    h3 = Hand.load([5, 8, 9, 6, 4])
    h4 = Hand.load([10, 20, 31, 25, 4])
    h5 = Hand.load([7, 9, 8, 5, 14, 20])

    assert h1.score() == 12
    assert h2.score() == 12
    assert h3.score() == 12
    assert h4.score() == 90
    assert h5.score() == 46
