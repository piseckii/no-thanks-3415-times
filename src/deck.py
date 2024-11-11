from src.card import Card

import random


class Deck:
    def __init__(self, cards: list[Card] | None = None):
        if cards == None:
            cards = Card.all_cards()

        self.cards: list[Card] = cards

    def __repr__(self):
        return f'{self.cards}'

    def __eq__(self, other):
        return self.cards == other.cards

    def save(self) -> list[int]:
        return [Card.save(card) for card in self.cards]

    @classmethod
    def load(cls, ls: list[int]):
        return cls(cards=[Card.load(num) for num in ls])

    def draw_card(self):
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)

    def is_empty(self):
        return self == Deck([])
