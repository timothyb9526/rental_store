from datetime import datetime
from core import *


def load_inventory():

    return Inventory([
        Property('small cabin', 5, 60, 90),
        Property('medium cabin', 6, 150, 200),
        Property('large cabin', 3, 300, 400),
        Property('studio apartment', 4, 150, 200),
        Property('medium apartment', 3, 200, 300),
        Property('penthouse', 1, 300, 400)
    ])


def get_inventory():
    with open('inventory.txt') as file:
        contents = file.readlines()
        return contents


def give_inventory(inventory):
    with open('inventory.txt', 'w') as file:
        file.write(inventory)


def write_to_log(rent):
    time = datetime.now()
    text = '\n{},\n{}'.format(time, rent.__str__())
    with open('history.txt', 'a') as file:
        file.write(text)


def employee():
    with open('history.txt') as file:
        files = file.read()

    print(files)
