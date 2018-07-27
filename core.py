class Property:
    def __init__(self, name, stock, rent, replacement):

        self.name = name
        self.stock = stock
        self.rent = rent
        self.replacement = replacement

    def rent(self):
        return self.rent

    def matches_name(self, name):

        return self.name.lower().startswith(name.lower())

    def history_string(self):
        return '{}, {}, {}, {}'.format(self.name, self.stock, self.rent,
                                       self.replacement)

    def __str__(self):

        return '{}: ${} per month'.format(self.name, self.rent)


class Inventory:
    def __init__(self, properties):

        self.properties = properties

    def in_stock(self, name):

        item = self.get_item(name)
        return not (item is None)

    def get_item(self, name):
        for item in self.properties:
            if item.matches_name(name):
                item.stock -= 1
                return item

    def update_stock(self):

        inventory = ''
        for property in self.properties:
            inventory += '\n{}'.format(property.history_string())

        return inventory

    def __str__(self):

        return 'Properties:\n{}'.format('\n'.join(map(str, self.properties)))


class Rental:
    def __init__(self, name, items):

        self.name = name
        self.items = items

    def add_item(self, item):

        self.items.append(item)

    def total(self):

        for i in self.items:

            price = (i.rent + self.replacement()) * 1.07

            return price

    def replacement(self):

        for i in self.items:

            return round(i.replacement * .10, 2)

    def __str__(self):
        return '-----------------\nCustomer: {}\nDeposit: {}\nTotal: ${:.2f}\nProperty: {}\n----------------'.format(
            self.name, self.replacement(), self.total(),
            ''.join('\n' + str(i) for i in self.items))

    def __repr__(self):
        return 'Rental({},{})'.format(repr(self.name), repr(self.items))
