from core import *
from disk import *


def user(inv, file, name, customer_employee):

    rent = Rental(name, [])

    while True:
        if customer_employee == 'Customer':
            print(inv)

            rental = input('Which would you like to rent today? ')

            item = inv.get_item(rental)
            rentals = rent.add_item(item)

            options = input('Would you like to checkout or continue? ')

            if options == 'checkout':

                for line in file:

                    if rental.lower() in line.lower():
                        print('-----------------')
                        print(rent)
                break
            elif options == 'continue':
                continue
            elif options == 'q':
                break

        elif customer_employee == 'Employee':
            employee()
        break


def main():

    inv = Inventory([
        Cabin('small cabin', 5, 60, 90),
        Cabin('medium cabin', 6, 150, 200),
        Cabin('large cabin', 3, 300, 400)
    ], [
        Appartment('studio appartment', 4, 150, 200),
        Appartment('medium appartment', 3, 200, 300),
        Appartment('penthouse', 1, 300, 400)
    ])

    file = get_inventory()

    print('Welcome to my rental agency press "q" to quit at any time.')
    customer_employee = input('Are you a customer or an employee? ')
    name = input('What name would be on this rental? ')

    user(inv, file, name, customer_employee)


if __name__ == '__main__':
    main()
