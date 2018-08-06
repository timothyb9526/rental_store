from datetime import datetime
from core import *


def load_inventory(contents, string):

    name, stock, rent, replacement = string.split(',')
    return Property(name, int(stock), int(rent), int(replacement))


def get_inventory():
    with open('inventory.txt') as file:
        contents = file.readline().split(',')
        lines = file.readlines()
    properties = []
    for l in lines:

        p = load_inventory(contents, l)
        properties.append(p)

    return Inventory(properties)


def give_inventory(inventory):
    with open('inventory.txt', 'w') as file:
        files = file.write(inventory)


def write_to_log(rent):
    time = datetime.now()
    text = '\n{},\n{}'.format(time, rent.__str__())
    with open('history.txt', 'a') as file:
        file.write(text)


def employee():
    with open('history.txt') as file:
        files = file.read()

    print(files)
