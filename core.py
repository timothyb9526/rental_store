class Movie:
    def __init__(self, name, stock, rent, replacement):

        self.name = name
        self.stock = stock
        self.rent = rent
        self.replacement = replacement

    def __str__(self):

        return '{}: ${} per day ({} in stock)'.format(self.name, self.rent,
                                                      self.stock)


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

        return 'Movies:\n{}\nBooks:\n{}'.format(
            '\n'.join(map(str, self.pizzas)), '\n'.join(map(str, self.sides)))
