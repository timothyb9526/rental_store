from core import *
from disk import *


def user(inv, file):

    print('Welcome to my rental agency press "q" to quit at any time.')

    customer_employee = input('Are you a customer or an employee? ')
    while True:
        if customer_employee == 'Customer':
            print(inv)

            rental = input('Which would you like to rent today? ')

            options = input('Would you like to checkout or quit? ')

            if options == 'checkout':

                name = input('What name would be on this rental? ')

                rent = Rental(name, [])

                item = inv.get_item(rental)
                rentals = rent.add_item(item)

                for line in file:

                    if rental.lower() in line.lower():
                        print('-----------------')
                        print(rent)
                break
            elif options == 'quit':
                break
            else:
                continue

        elif customer_employee == 'Employee':
            employee(customer_employee)


def main():

    inv = Inventory([
        Movie('The Purge', 5, 4, 10),
        Movie('Deadpool', 6, 5, 12),
        Movie('Wind River', 3, 4, 16)
    ], [Book('Lonesome Dove', 4, 5, 7),
        Book('The Great Gatsby', 3, 6, 10)])

    file = get_inventory()

    user(inv, file)


if __name__ == '__main__':
    main()
