from core import *

# -------------------------------------Property-----------------------------------------


def test_Property_init_():

    p = Property('small cabin', 5, 100, 150)

    assert p.name == 'small cabin'
    assert p.stock == 5
    assert p.rent == 100
    assert p.replacement == 150


def test_small_cabin_matches_name():

    p = Property('small cabin', 5, 100, 150)

    assert p.matches_name('small cabin')


def test_Property_history_str():
    p = Property('small cabin', 5, 100, 150)

    assert p.history_string() == 'small cabin, 5, 100, 150'


def test_Property_str():

    p = Property('small cabin', 5, 100, 150)

    assert p.__str__() == 'small cabin: $100 per month'


# ------------------------------------Inventory----------------------------------------


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


def test_return_item():

    properties = [
        Property('small cabin', 5, 100, 150),
        Property('medium cabin', 6, 150, 200),
        Property('large cabin', 3, 300, 400),
        Property('studio apartment', 4, 150, 200),
        Property('medium apartment', 3, 200, 300),
        Property('penthouse', 1, 400, 800)
    ]

    inv = Inventory(properties)

    item = inv.return_item('small cabin')
    assert item.stock == 6
    assert item.name == 'small cabin'


def test_rent_item():

    properties = [
        Property('small cabin', 5, 100, 150),
        Property('medium cabin', 6, 150, 200),
        Property('large cabin', 3, 300, 400),
        Property('studio apartment', 4, 150, 200),
        Property('medium apartment', 3, 200, 300),
        Property('penthouse', 1, 400, 800)
    ]

    inv = Inventory(properties)

    item = inv.rent_item(0)
    assert item.stock == 4
    assert item.name == 'small cabin'


def test_update_stock():
    properties = [
        Property('small cabin', 5, 100, 150),
    ]

    inv = Inventory(properties)

    assert inv.update_stock() == '\nsmall cabin, 5, 100, 150'


def test_get_item():

    properties = [
        Property('small cabin', 5, 100, 150),
    ]

    inv = Inventory(properties)

    assert inv.__getitem__(0) == inv.rent_item(0)


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


# ---------------------------------Rental-----------------------------------------------


def test_rental_init():

    R = Rental('timothy', ['small cabin'], '3', 'rent')

    assert R.name == 'timothy'
    assert R.items == ['small cabin']
    assert R.length == '3'
    assert R.type == 'rent'


def test_add_item():

    R = Rental('Timothy', [], '3', 'rent')

    R.add_item(Property('small cabin', 5, 100, 150))

    assert len(R.items) == 1


def test_rental_return_str():
    R = Rental('timothy', [Property('small cabin', 5, 100, 150)], '3', 'C')

    assert R.return_string(
    ) == '-----------------\nType: C\nCustomer: timothy\nDeposit: 15.0\nTotal: $321.00 for 3 months\nProperty: \nsmall cabin: $100 per month\n----------------'


def test_log_string():

    R = Rental('timothy', [Property('small cabin', 5, 100, 150)], '3', 'R')

    assert R.log_string(
    ) == '\nR, timothy, 15.0, 336.0, small cabin: $100 per month, 336.0\n'


def test_return_log():

    R = Rental('timothy', [Property('small cabin', 5, 100, 150)], '3', 'C')

    assert R.return_log(
    ) == '\nC, timothy, 15.0, 321.0, small cabin: $100 per month, 321.0\n'


def test_rental_str():

    R = Rental('timothy', [Property('small cabin', 5, 100, 150)], '3', 'R')

    assert R.__str__(
    ) == '-----------------\nType: R\nCustomer: timothy\nDeposit: 15.0\nTotal: $336.00 for 3 months\nProperty: \nsmall cabin: $100 per month\n-----------------'


def test_repr():

    R = Rental('Timothy', [], '3', 'R')

    assert repr(R) == 'Rental(\'Timothy\',[],\'R\')'
