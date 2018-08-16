class Property:
    def __init__(self, name, stock, rent, replacement):

        self.name = name
        self.stock = stock
        self.rent = rent
        self.replacement = replacement

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

    def return_item(self, name):
        for item in self.properties:
            if item.matches_name(name):
                item.stock += 1
                return item

    def rent_item(self, index):
        item = self.properties[index]
        item.stock -= 1
        return item

    def __getitem__(self, item):
        return self.rent_item(item)

    def update_stock(self):
        inventory = ''
        for property in self.properties:
            inventory += '\n{}'.format(property.history_string())

        return inventory

    def __str__(self):

        return 'Properties:\n{}'.format('\n'.join(map(str, self.properties)))


class Rental:
    def __init__(self, name, items, length, type):

        self.name = name
        self.items = items
        self.length = length
        self.type = type

    def add_item(self, item):

        self.items.append(item)

    def total_minus_deposit(self):

        for i in self.items:

            price = i.rent * 1.07

            return (price * int(self.length))

    # def revenue(self):
    #     total_revenue = []
    #     for i in self.items:
    #         cost = i.rent
    #         total_revenue.append(cost)
    #         total = sum(total_revenue)
    #     return total

    def return_string(self):
        return '-----------------\nType: {}\nCustomer: {}\nDeposit: {}\nTotal: ${:.2f} for {} months\nProperty: {}\n----------------'.format(
            self.type, self.name, self.replacement(),
            self.total_minus_deposit(), self.length, ''.join(
                '\n' + str(i) for i in self.items))

    def return_log(self):
        base_string = '{}, {}, {}, {}'.format(self.type, self.name,
                                              self.replacement(),
                                              self.total_minus_deposit())
        end_string = ', '.join(str(i) for i in self.items)
        return base_string + ', ' + end_string + ', ' + str(
            self.total_minus_deposit()) + '\n'

    def log_string(self):
        base_string = '{}, {}, {}, {}'.format(self.type, self.name,
                                              self.replacement(), self.total())
        end_string = ', '.join(str(i) for i in self.items)
        return base_string + ', ' + end_string + ', ' + str(
            self.total()) + '\n'

    def total(self):

        for i in self.items:

            price = i.rent * 1.07

            return (price * int(self.length)) + self.replacement()

    def replacement(self):
        for i in self.items:
            return round(i.replacement * .10, 2)

    def __str__(self):

        return '-----------------\nType: {}\nCustomer: {}\nDeposit: {}\nTotal: ${:.2f} for {} months\nProperty: {}\n-----------------'.format(
            self.type, self.name, self.replacement(), self.total(),
            self.length, ''.join('\n' + str(i) for i in self.items))

    def __repr__(self):
        return 'Rental({},{},{})'.format(
            repr(self.name), repr(self.items), repr(self.type))
