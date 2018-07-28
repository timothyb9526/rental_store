from core import *


def test_Property_init_():

    p = Property('small cabin', 5, 60, 90)

    assert p.name == 'small cabin'
    assert p.stock == 5
    assert p.rent == 60
    assert p.replacement == 90


def test_Property_rent():

    p = Property('small cabin', 5, 60, 90)

    assert p.rent == 60


def test_Property_matches_name():

    p = Property('small cabin', 5, 60, 90)

    assert p.name == 'small cabin'


def test_Property_str():

    p = Property('small cabin', 5, 60, 90)

    assert p == 'small cabin: $60 per month'
