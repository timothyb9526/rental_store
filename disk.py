from datetime import datetime


def get_inventory():
    with open('inventory.txt') as file:
        contents = file.readlines()
        return contents


def give_inventory(text):
    with open('inventory.txt', 'w') as file:

        file.write(text)


def write_to_log(item, rent):
    time = datetime.now()
    text = '\n{}, {}, {}'.format(time, item, rent)
    with open('history.txt', 'a') as file:
        file.write(text)


def employee():
    with open('history.txt') as file:
        files = file.read()

    print(files)

    exit()
