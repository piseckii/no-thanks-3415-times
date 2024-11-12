from abc import ABC, abstractmethod

from src.card import Card
from src.hand import Hand
from src.player import Player
import enum


class Action(enum.StrEnum):
    PAY = 'pay'
    TAKE_CARD = 'take card'


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
        print(f'{player.name}({cls.__name__}): pays')

    @classmethod
    def inform_card_is_taken(cls, player: Player):
        """
        Сообщает, что игрок взял карту.
        """
        print(f'{player.name}({cls.__name__}): takes card')
