import typing

from src.card import Card
from src.deck import Deck
from src.player import Player
from src.top import Top


class GameState:
    def __init__(self, players: list[Player], deck: Deck, top: Top, current_player: int = 0):
        self.players: list[Player] = players
        self.deck: Deck = deck
        self.top: Top = top
        self._current_player: int = current_player

    def __repr__(self):
        return f"""
          "top": {self.top},
          "deck": {self.deck},
          "current_player_index": {self._current_player},
          "players": {[p.save() for p in self.players]}"""

    def current_player(self) -> Player:
        return self.players[self._current_player]

    def __eq__(self, other):
        return self.players == other.players and self.deck == other.deck and self.top == other.top and \
            self._current_player == other._current_player

    def save(self) -> dict:
        return {
            "top": self.top.save(),
            "deck": self.deck.save(),
            "current_player_index": self._current_player,
            "players": [p.save() for p in self.players]
        }

    @classmethod
    def load(cls, data: dict):
        players = [Player.load(d) for d in data['players']]

        return cls(
            players=players,
            deck=Deck.load(data['deck']),
            top=Top.load(data['top']),
            current_player=int(data['current_player_index']))

    def next_player(self):
        n = len(self.players)
        self._current_player = (self._current_player + 1) % n

    def draw_card(self):
        """Текущий игрок берет карту из колоды."""
        card = self.deck.draw_card()
        self.current_player().hand.add_card(card)
