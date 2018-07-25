class Cabin:
    def __init__(self, name, stock, rent, replacement):

        self.name = name
        self.stock = stock
        self.rent = rent
        self.replacement = replacement

    def rent(self):
        return self.rent

    def matches_name(self, name):

        return self.name.lower().startswith(name.lower())

    def __str__(self):

        return '{}: ${} per day ({} available)'.format(self.name, self.rent,
                                                       self.stock)


class Appartment:
    def __init__(self, name, stock, rent, replacement):

        self.name = name
        self.stock = stock
        self.rent = rent
        self.replacement = replacement

    def rent(self):
        return self.rent

    def matches_name(self, name):

        return self.name.lower().startswith(name.lower())

    def __str__(self):

        return '{}: ${} per month ({} available)'.format(
            self.name, self.rent, self.stock)


class Inventory:
    def __init__(self, movies, books):

        self.movies = movies
        self.books = books

    def in_stock(self, name):

        item = self.get_item(name)
        return not (item is None)

    def get_item(self, name):
        for item in self.movies + self.books:
            if item.matches_name(name):
                return item

    def __str__(self):

        return 'Cabins:\n{}\nApartments:\n{}'.format(
            '\n'.join(map(str, self.movies)), '\n'.join(map(str, self.books)))


class Rental:
    def __init__(self, name, items):

        self.name = name
        self.items = items

    def add_item(self, item):

        self.items.append(item)

    def total(self):

        for i in self.items:

            price = (i.rent + self.replacement()) * .07

            return price + (i.rent + self.replacement())

    def replacement(self):

        for i in self.items:

            return round(i.replacement * .10, 2)

    def __str__(self):
        return 'Customer: {}\nReplacement: {}\nTotal: ${:.2f}\nItems:\n{}\n----------------'.format(
            self.name, self.replacement(), self.total(),
            ''.join('\n' + str(i) for i in self.items))

    def __repr__(self):
        return 'Rental({},{})'.format(repr(self.name), repr(self.items))
