from src.hand import Hand
from src.player import Player


def test_init():
    h = Hand.load([4, 5, 6])
    p = Player('Noob', h, 15)
    assert p.name == 'Noob'
    assert p.hand == h
    assert p.jeton == 15

def test_repr():
    h = Hand.load([4, 5, 6])
    p = Player(name='Alex', hand=h, jeton=15)
    assert str(p) == 'Alex(15): [|4|, |5|, |6|]'
    assert repr(p) == 'Alex(15): [|4|, |5|, |6|]'
    
    
def test_save():
    h = Hand.load([4, 5, 6])
    p = Player(name='Alex', hand=h, jeton=15)
    assert p.save() == {'name': 'Alex', 'hand': [4, 5, 6], 'jeton': 15}

def test_eq():
    h1 = Hand.load([4, 5, 6])
    h2 = Hand.load([4, 5, 6])
    p1 = Player(name='Alex', hand=h1, jeton=15)
    p2 = Player(name='Alex', hand=h2, jeton=15)
    assert p1 == p2

def test_load():
    data = {'name': 'Alex', 'hand': [4, 5, 6], 'jeton': 15}
    h = Hand.load([4, 5, 6])
    p_expected = Player(name='Alex', hand=h, jeton=15)
    p = Player.load(data)
    assert p == p_expected


def test_pay():
    data = {'name': 'PlayerUnknown', 'hand': [4, 5, 6], 'jeton': 15}
    p = Player.load(data)
    
    p.pay()
    
    assert p.jeton == 14
    assert p.pay() == 1
    assert p.jeton == 13