from src.card import Card
from src.hand import Hand
from src.player import Player

from src.player_interaction import PlayerInteraction
from player_interaction import Action


class Human(PlayerInteraction):
    @classmethod
    def choose_action(cls, player: Player, ):
        while True:
            action = input('Choose action:\n')
            match action:
                case 't':
                    action = Action.TAKE_CARD
                    return action
                case 'p':
                    action = Action.PAY

                    if action == 'p' and player.chips <= 0:
                        print('You forced to take card (have no chips)')
                        action = Action.TAKE_CARD
                    return action

            print('Please type "t" to take card or "p" for pay')
