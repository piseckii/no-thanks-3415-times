from src.card import Card


class Top:
    def __init__(self, card: Card | None = None, chips: int = 0):
        self.card = card
        self.chips = chips

    def __repr__(self):
        return f'{self.card} chips: {self.chips}'

    def __eq__(self, other):
        return self.card == other.card and self.chips == other.chips

    def save(self) -> dict:
        return {'card': self.card.save(), 'chips': self.chips}

    @classmethod
    def load(cls, d: dict):
        return cls(card=Card.load(d['card']), chips=d['chips'])

    def change_card(self, card=Card):
        self.card = card
        self.chips = 0
