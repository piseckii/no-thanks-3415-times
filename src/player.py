from src.hand import Hand

import json
import typing


class Player:
    def __init__(self, name: str, hand: Hand, jeton: int = 11):
        self.name = name
        self.hand = hand
        self.jeton = jeton

    def __repr__(self):
        return f'{self.name}({self.jeton}): {self.hand}'

    def __eq__(self, other: typing.Self | str | dict):
        if isinstance(other, str):
            other = self.load(json.loads(other))
        if isinstance(other, dict):
            other = self.load(other)
        return self.name == other.name \
               and self.jeton == other.jeton \
               and self.hand == other.hand

    def save(self) -> dict:
        return {
            'name': self.name,
            'hand':  Hand.save(self.hand),
            'jeton': self.jeton
        }

    @classmethod
    def load(cls, data: dict):
        return cls(name=data['name'], hand=Hand.load(data['hand']), jeton=int(data['jeton']))
    
    def pay(self):
        self.jeton -= 1
        return 1
        