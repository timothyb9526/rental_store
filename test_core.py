from core import *


def test_Property_init_():

    p = Property('small cabin', 5, 100, 150)

    assert p.name == 'small cabin'
    assert p.stock == 5
    assert p.rent == 100
    assert p.replacement == 150


def test_small_cabin_rent():

    p = Property('small cabin', 5, 100, 150)

    assert p.rent == 100


def test_medium_cabin_rent():

    p = Property('medium cabin', 5, 150, 200)

    assert p.rent == 150


def test_large_cabin_rent():

    p = Property('large cabin', 5, 300, 400)

    assert p.rent == 300


def test_studio_apartment_rent():

    p = Property('studio apartment', 5, 300, 400)

    assert p.rent == 300


def test_medium_apartment_rent():

    p = Property('medium apartment', 5, 300, 400)

    assert p.rent == 300


def test_penthouse_rent():

    p = Property('penthouse', 5, 300, 400)

    assert p.rent == 300


def test_small_cabin_matches_name():

    p = Property('small cabin', 5, 100, 150)

    assert p.name == 'small cabin'


def test_medium_cabin_matches_name():

    p = Property('medium cabin', 5, 100, 150)

    assert p.name == 'medium cabin'


def test_large_cabin_matches_name():

    p = Property('large cabin', 5, 100, 150)

    assert p.name == 'large cabin'


def test_studio_apartment_matches_name():

    p = Property('studio apartment', 5, 100, 150)

    assert p.name == 'studio apartment'


def test_Property_matches_name():

    p = Property('medium apartment', 5, 100, 150)

    assert p.name == 'medium apartment'


def test_Penthouse_matches_name():

    p = Property('penthouse', 5, 100, 150)

    assert p.name == 'penthouse'


def test_Property_history_str():
    p = Property('small cabin', 5, 100, 150)

    assert p.history_string() == 'small cabin, 5, 100, 150'


def test_Property_str():

    p = Property('small cabin', 5, 100, 150)

    assert p.__str__() == 'small cabin: $100 per month'


def test_inventory_init_():
    properties = [
        Property('small cabin', 5, 100, 150),
        Property('medium cabin', 6, 150, 200),
        Property('large cabin', 3, 300, 400),
        Property('studio apartment', 4, 150, 200),
        Property('medium apartment', 3, 200, 300),
        Property('penthouse', 1, 400, 800)
    ]

    inv = Inventory(properties)

    assert inv.properties == properties


def test_inventory_str():

    properties = [
        Property('small cabin', 5, 100, 150),
        Property('medium cabin', 6, 150, 200),
        Property('large cabin', 3, 300, 400),
        Property('studio apartment', 4, 150, 200),
        Property('medium apartment', 3, 200, 300),
        Property('penthouse', 1, 400, 800)
    ]

    inv = Inventory(properties)

    assert inv.__str__(
    ) == 'Properties:\nsmall cabin: $100 per month\nmedium cabin: $150 per month\nlarge cabin: $300 per month\nstudio apartment: $150 per month\nmedium apartment: $200 per month\npenthouse: $400 per month'


def test_rental_init():

    R = Rental('timothy', ['small cabin'], '3', 'rent')

    assert R.name == 'timothy'
    assert R.items == ['small cabin']
    assert R.length == '3'
    assert R.type == 'rent'


def test_rental_return_str():
    R = Rental('timothy', [Property('small cabin', 5, 100, 150)], '3', 'C')

    assert R.return_string(
    ) == '-----------------\nType: C\nCustomer: timothy\nDeposit: 15.0\nTotal: $321.00 for 3 months\nProperty: \nsmall cabin: $100 per month\n----------------'


def test_rental_str():

    R = Rental('timothy', [Property('small cabin', 5, 100, 150)], '3', 'R')

    assert R.__str__(
    ) == '-----------------\nType: R\nCustomer: timothy\nDeposit: 15.0\nTotal: $336.00 for 3 months\nProperty: \nsmall cabin: $100 per month\n-----------------'
