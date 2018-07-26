from core import *
from disk import *


def user(inv, file, name, customer_employee):

    rent = Rental(name, [])

    while True:
        if customer_employee == 'Customer':
            print(inv)
            print()

            rental = input('Which would you like to rent today? ')
            print()

            item = inv.get_item(rental)
            rentals = rent.add_item(item)

            options = input('Would you like to checkout or continue? ')
            print()

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
    inv = load_inventory()

    give_inventory()

    file = get_inventory()

    print('Welcome to my rental agency press "q" to quit at any time.')
    print()
    customer_employee = input('Are you a customer or an employee? ')
    print()
    name = input('What name would be on this rental? ')

    user(inv, file, name, customer_employee)

    write_to_log()


if __name__ == '__main__':
    main()
