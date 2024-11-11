from src.card import Card
from src.hand import Hand
from src.player import Player

from src.player_interaction import PlayerInteraction


class Human(PlayerInteraction):
    @classmethod
    def choose_action(cls, player: Player, ):
        while True:
            action = input('Choose action:\n')

            if action in ('take card', 'pay'):
                if action == 'pay' and player.chips <= 0:
                    print('You have not enough chips!')
                    continue
                return action

            print('Please type "take card" or "pay"')

    @classmethod
    def inform_player_paid(cls, player: Player):
        """
        Сообщает, что игрок заплатил фишку.
        """
        print(f'{player.name}: pays')

    @classmethod
    def inform_card_is_taken(cls, player: Player):
        """
        Сообщает, что игрок взял карту.
        """
        print(f'{player.name}: takes card')
