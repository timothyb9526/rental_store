from core import *
from disk import *


def user(inv, file, customer_employee):

    while True:
        if customer_employee == 'Customer':
            print(inv)
            print()
            name = input('What name would be on this rental? ')

            print()
            rental = input('Which would you like to rent today? ')
            print()

            rental_length = input('How long would you like to start renting? ')
            print()

            rent = Rental(name, [], rental_length)
            item = inv.get_item(rental)
            rentals = rent.add_item(item)
            print('Thanks for your business.')
            print()

            for line in file:

                if rental.lower() in line.lower():

                    print(rent)

        elif customer_employee == 'Employee'.lower():
            employee()
        break


def main():
    inv = load_inventory()

    file = get_inventory()

    print('Welcome to my rental agency press "q" to quit at any time.')
    print()
    customer_employee = input('Are you a customer or an employee? ')
    print()

    rent = user(inv, file, customer_employee)

    write_to_log(rent)
    inventory = inv.update_stock()
    give_inventory(inventory)


if __name__ == '__main__':
    main()
