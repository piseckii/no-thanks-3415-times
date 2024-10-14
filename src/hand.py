from src.card import Card


class Hand:
    def __init__(self, cards: list[Card] | None = None):
        if cards == None:
            cards = []

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

    def add_card(self, card: Card):
        self.cards.append(card)
        return self

    def score(self) -> int:
        h = [card.value for card in self.cards]
        h.sort()
        s = 0
        for i in range(len(h)):
            if (h[i] == h[i-1] + 1) and i != 0:
                continue
            s += h[i]
        return s
