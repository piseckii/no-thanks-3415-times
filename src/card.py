class Card:
    VALUES = list(range(3, 36))

    def __init__(self, value: int):
        if value not in Card.VALUES:
            raise ValueError
        self.value = value

    def __repr__(self):
        return f'|{self.value}|'

    def __eq__(self, other):
        return self.value == other.value

    def save(self) -> int:
        return self.value

    @classmethod
    def load(cls, num: int):
        return cls(num)

    @classmethod
    def all_cards(cls, values: None | list[int] = None):
        if values is None:
            values = cls.VALUES
        cards = [cls(val) for val in values]
        return cards
