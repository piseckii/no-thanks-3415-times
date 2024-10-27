from abc import ABC, abstractmethod

from src.card import Card
from src.hand import Hand
from src.player import Player


class PlayerInteraction(ABC):
    @classmethod
    @abstractmethod
    def choose_action(cls) -> Card:
        '''Игрок выбирает взять карту или заплатить фишку'''
        pass

    @classmethod
    def inform_player_paid(cls, player: Player):
        """
        Сообщает, что игрок заплатил фишку.
        """
        pass

    @classmethod
    def inform_card_is_taken(cls, player: Player):
        """
        Сообщает, что игрок взял карту.
        """
        pass
