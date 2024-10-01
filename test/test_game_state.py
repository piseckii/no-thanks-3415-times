import pytest

from src.card import Card
from src.deck import Deck
from src.hand import Hand
from src.top import Top
from src.game_state import GameState
from src.player import Player

data = {
    'top': 
        {
            'card': 23,
            'chips': 35
        },
    'current_player_index': 1,
    'deck': [11, 18],
    'players': [
        {
            'name': 'Alex',
            'hand': [7, 19, 30, 32],
            'chips': 5
        },
        {
            'name': 'Bob',
            'hand': [8, 6, 14],
            'chips': 1
        },
        {
            'name': 'Charley',
            'hand': [5, 10, 15],
            'chips': 3
        }
    ]
}

alex = Player.load(data['players'][0])
bob = Player.load(data['players'][1])
charley = Player.load(data['players'][2])
full_deck = Deck(None)


def test_init():
    players = [alex, bob, charley]
    game = GameState(players=players, deck=full_deck, current_player=1, top=Top(Card(5)))
    
    assert game.players == players
    assert game.deck == full_deck
    assert game._current_player == 1
    assert game.top == Top(Card.load(5))
    assert game.top.chips == 0


def test_current_player():
    players = [alex, bob, charley]
    game = GameState(players=players, deck=full_deck, top=Top(Card(7)))
    assert game.current_player() == alex

    game = GameState(players=players, deck=full_deck, top=Top(Card(7)), current_player=1)
    assert game.current_player() == bob

    game = GameState(players=players, deck=full_deck, top=Top(Card(7)), current_player=2)
    assert game.current_player() == charley


def test_eq():
    players = [alex, bob, charley]
    
    game1 = GameState(players=players, deck=full_deck, top=Top(Card(7)))
    game2 = GameState(players=players.copy(), deck=Deck(None), top=Top(Card(7)))
    game3 = GameState(players=players, deck=Deck.load([5, 6, 7]), top=Top(Card(7)))
    
    assert game1 == game2
    assert game1 != game3


def test_save():
    players = [alex, bob, charley]
    game = GameState(players=players, deck=Deck.load(data['deck']), top=Top.load(data['top']), current_player=1)
    assert game.save() == data


def test_load():
    game = GameState.load(data)
    assert game.save() == data


def test_next_player():
    game = GameState.load(data)
    assert game.current_player() == bob

    game.next_player()
    assert game.current_player() == charley

    game.next_player()
    assert game.current_player() == alex

    game.next_player()
    assert game.current_player() == bob


def test_draw_card():
    game = GameState.load(data)
    
    assert game.deck == Deck.load([11, 18])
    assert game.current_player().hand == Hand.load([8, 6, 14])

    game.draw_card()
    assert game.deck ==  Deck.load([18])
    assert game.current_player().hand == Hand.load([8, 6, 14, 11])