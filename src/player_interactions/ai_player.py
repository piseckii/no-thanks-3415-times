from src.card import Card
from src.player import Player

from src.player_interaction import PlayerInteraction


class Bot(PlayerInteraction):
    @classmethod
    def choose_action(cls, player: Player, ):
        if player.chips < 2:
            action = 'take card'
        elif len(player.hand) < 2:
            action = 'take card'
        else:
            action = 'pay'
        return action

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
