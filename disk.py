def get_inventory():
    with open('inventory.txt') as file:
        contents = file.readlines()
        print(contents)
        return contents
