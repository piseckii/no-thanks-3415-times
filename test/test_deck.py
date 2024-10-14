import pytest
import random

from src.card import Card
from src.deck import Deck


def test_init():
    cards = [Card(12), Card(15), Card(16)]

    d = Deck(cards)

    assert d.cards == cards


def test_repr():
    cards = [Card(12), Card(15), Card(16)]

    d = Deck(cards)
    d1 = Deck([Card(9)])

    assert d.__repr__() == "[|12|, |15|, |16|]"
    assert d1.__repr__() == "[|9|]"
    assert Deck([Card(4)]).__repr__() == "[|4|]"


def test_eq():
    cards = [Card(12), Card(15), Card(16)]

    d = Deck(cards)
    d1 = Deck(cards)
    d2 = Deck([Card(12), Card(15), Card(16)])
    d3 = Deck([Card(4), Card(5)])

    assert d == d1
    assert d == d2
    assert d != d3


def test_save():
    cards = [Card(12), Card(15), Card(16)]

    d = Deck(cards)

    assert d.save() == [12, 15, 16]
    assert Deck(cards).save() == [12, 15, 16]
    assert Deck([Card(3)]).save() == [3]


def test_load():
    cards = [Card(12), Card(15), Card(16)]

    d = Deck(cards).save()

    assert Deck.load(d) == Deck(cards)
    assert Deck.load([12]) == Deck([Card(12)])


def test_draw_card():
    cards = [Card(12), Card(14), Card(16)]

    d = Deck(cards)

    assert d.draw_card() == Card(12)
    assert d == Deck([Card(14), Card(16)])


def test_shuffle():
    random.seed(3)

    cards = Card.all_cards([7, 9, 8, 10, 11])
    deck = Deck(cards)

    deck.shuffle()
    assert deck.save() == [7, 8, 10, 11, 9]

    deck.shuffle()
    assert deck.save() == [8, 11, 10, 7, 9]

    deck.shuffle()
    assert deck.save() == [11, 8, 9, 10, 7]
