from src.hand import Hand
from src.player import Player


def test_init():
    h = Hand.load([4, 5, 6])
    p = Player('Noob', h, 15)
    assert p.name == 'Noob'
    assert p.hand == h
    assert p.chips == 15


def test_repr():
    h = Hand.load([4, 5, 6])
    p = Player(name='Alex', hand=h, chips=15)
    assert str(p) == 'Alex(15): [|4|, |5|, |6|]'
    assert repr(p) == 'Alex(15): [|4|, |5|, |6|]'


def test_save():
    h = Hand.load([4, 5, 6])
    p = Player(name='Alex', hand=h, chips=15)
    assert p.save() == {'name': 'Alex', 'hand': [4, 5, 6], 'chips': 15}


def test_eq():
    h1 = Hand.load([4, 5, 6])
    h2 = Hand.load([4, 5, 6])
    p1 = Player(name='Alex', hand=h1, chips=15)
    p2 = Player(name='Alex', hand=h2, chips=15)
    assert p1 == p2


def test_load():
    data1 = {'name': 'Alex', 'hand': [4, 5, 6], 'chips': 15}
    h = Hand.load([4, 5, 6])
    data2 = {'name': 'Alex', 'hand': [4, 5, 6]}

    p1_expected = Player(name='Alex', hand=h, chips=15)
    p1 = Player.load(data1)

    p2 = Player.load(data2)
    p2_expected = Player('Alex', Hand.load([4, 5, 6]))

    assert p1 == p1_expected
    assert p2 == p2_expected
