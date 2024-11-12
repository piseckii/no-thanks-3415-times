from src.card import Card
from src.player import Player

from src.player_interaction import PlayerInteraction
import random

from player_interaction import Action


class Bot(PlayerInteraction):
    @classmethod
    def choose_action(cls, player: Player, ):
        if player.chips <= 0:
            action = Action.TAKE_CARD
        else:
            action = random.choice((Action.TAKE_CARD, Action.PAY))
        return action

    @classmethod
    def inform_player_paid(cls, player: Player):
        """
        Сообщает, что игрок заплатил фишку.
        """
        print(f'{player.name}(Bot): pays')

    @classmethod
    def inform_card_is_taken(cls, player: Player):
        """
        Сообщает, что игрок взял карту.
        """
        print(f'{player.name}(Bot): takes card')
