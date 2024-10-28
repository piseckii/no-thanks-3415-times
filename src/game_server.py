import inspect
import json
import sys

from src.deck import Deck
from src.top import Top
from src.game_state import GameState
from src.hand import Hand
from src.player import Player
from src.player_interaction import PlayerInteraction
import src.player_interactions as all_player_types

import logging

import enum


# class GamePhase(enum.StrEnum):
#     CHOOSE_CARD = "Choose card"
#     DRAW_EXTRA = "Draw extra card"
#     NEXT_PLAYER = "Switch current player"
#     DECLARE_WINNER = "Declare a winner"
#     GAME_END = "Game ended"

class GamePhase(enum.StrEnum):
    BIDDING = "Choose to pay or take card"
    NEXT_CARD = "Take card from deck and place on the top"
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"


class GameServer:

    def __init__(self, player_types, game_state):
        self.game_state: GameState = game_state
        self.player_types: dict = player_types  # {player: PlayerInteractions}

    @classmethod
    def load_game(cls):
        # TODO: выбрать имя файла
        filename = 'no_thanks.json'
        with open(filename, 'r') as fin:
            data = json.load(fin)
            game_state = GameState.load(data)
            print(game_state.save())
            player_types = {}
            for player, player_data in zip(game_state.players, data['players']):
                kind = player_data['kind']
                kind = getattr(all_player_types, kind)
                player_types[player] = kind
            return GameServer(player_types=player_types, game_state=game_state)

    def save(self):
        filename = 'no_thanks.json'
        data = self.save_to_dict()
        with open(filename, 'w') as fout:
            json.dump(data, fout, indent=4)

    def save_to_dict(self):
        data = self.game_state.save()
        for player_index, player in enumerate(self.player_types.keys()):
            player_interaction = self.player_types[player]
            data['players'][player_index]['kind'] = self.player_types[player].__name__
        return data

    @classmethod
    def get_players(cls):
        player_count = cls.request_player_count()

        player_types = {}
        for p in range(player_count):
            name, kind = cls.request_player()
            player = Player(name, Hand())
            player_types[player] = kind
        return player_types

    @classmethod
    def new_game(cls, player_types: dict):
        # Shuffle the deck and remove 9 cards
        deck = Deck().shuffle()
        for _ in range(9):
            deck.draw_card()

        top = Top(deck.draw_card())
        game_state = GameState(list(player_types.keys()), deck, top)

        print(game_state.save())

        res = cls(player_types, game_state)
        return res

    def run(self):
        current_phase = GamePhase.BIDDING
        while current_phase != GamePhase.GAME_END:
            phases = {
                GamePhase.BIDDING: self.bidding_phase,
                GamePhase.NEXT_CARD: self.next_card_phase,
                GamePhase.DECLARE_WINNER: self.declare_winner_phase,
            }
            current_phase = phases[current_phase]()

    def declare_winner_phase(self) -> GamePhase:
        score = self.gamestate.score()
        w = min(score, key=lambda k: score[k])

        print('Score:')
        for key in score:
            print(key, score[key], sep='\t')
        print('Winner:')
        print(w, score[w], sep='\t')

        return GamePhase.GAME_END

    def next_card_phase(self) -> GamePhase:
        if not self.game_state.deck:
            return GamePhase.DECLARE_WINNER
        self.game_state.top = self.game_state.top.change_card(
            self.game_state.deck.draw_card())
        print('Top:', self.game_state.top)
        return GamePhase.BIDDING

    def bidding_phase(self) -> GamePhase:
        current_player = self.game_state.current_player()
        card_is_taken = False
        while not (card_is_taken):
            if PlayerInteraction.choose_action() == 'take card':
                self.game_state.take_card()
                card_is_taken = True
                PlayerInteraction.inform_card_is_taken()
            elif PlayerInteraction.choose_action() == 'pay':
                self.game_state.pay()
                PlayerInteraction.inform_player_paid()
        return GamePhase.NEXT_CARD

    def inform_all(self, method: str, *args, **kwargs):
        """
        Calls player_interaction.method with *args, **kwargs for all players

        self.inform_all(..., player, card=Card('g7'))
          args   : [player]
          kwargs : {"card":Card('g7')}

        self.inform_all(..., player=player, card=Card('g7'))
          args   : []
          kwargs : {"player":player, "card":Card('g7')}
        """
        for p in self.player_types.values():
            getattr(p, method)(*args, **kwargs)

    @staticmethod
    def request_player_count() -> int:
        while True:
            try:
                player_count = int(input("How many players?"))
                if 3 <= player_count <= 7:
                    return player_count
            except ValueError:
                pass
            print("Please input a number between 3 and 7")

    @staticmethod
    def request_player() -> (str, PlayerInteraction):
        """Возвращает имя и тип игрока."""

        """Разрешенные типы игроков из PlayerInteraction."""
        # Getting all names of subclasses of PlayerInteraction from  all_player_types
        player_types = []
        for name, cls in inspect.getmembers(all_player_types):
            if inspect.isclass(cls) and issubclass(cls, PlayerInteraction):
                player_types.append(cls.__name__)
        player_types_as_str = ', '.join(player_types)

        while True:
            name = input("How to call a player?")
            if name.isalpha():
                break
            print("Name must be a single word, alphabetic characters only")

        while True:
            try:
                kind = input(
                    f"What kind of player is it ({player_types_as_str})?")
                kind = getattr(all_player_types, kind)
                break
            except AttributeError:
                print(f"Allowed player types are: {player_types_as_str}")
        return name, kind


def __main__():
    load_from_file = False
    if load_from_file:
        server = GameServer.load_game()
        server.save()
    else:
        server = GameServer.new_game(GameServer.get_players())
    server.run()


if __name__ == "__main__":
    __main__()

__main__()
