from core import *
from disk import *


def user(inv, file, customer_employee):

    while input != 'q':
        if customer_employee == 'customer':

            rent_or_return = input(
                'Would you like to rent or close a current rental? ')
            print()
            if rent_or_return == 'rent':
                print(inv)
                print()

                rental = input('Which would you like to rent today? ')
                print()
                name = input('What name would be on this rental? ')
                print()

                rental_length = input('How long will you be renting? ')
                print()

                rent = Rental(name, [], rental_length, rent_or_return)
                item = inv.get_item(rental)
                rentals = rent.add_item(item)
                print('Thanks for your business.')
                print()

                for line in file:

                    if rental.lower() in line.lower():

                        print(rent)
                        return rent
            elif rent_or_return == 'close':

                return_item = input('What would you like to return? ')
                print()
                customer = input('What was the name? ')
                print()

                length = input('How long was the rental for? ')
                print()

                print('Thank you for your business.')
                print()

                return_list = Rental(customer, [], length, rent_or_return)
                item = inv.give_item(return_item)
                rentals = return_list.add_item(item)

                for line in file:
                    if return_item.lower() in line.lower():

                        print(return_list.return_string())
                        return return_list.return_string()

        elif customer_employee == 'employee':

            history = input(
                'Would you like to see the transaction history or the inventory? '
            )
            print()

            if history == 'history':

                employee()

            elif history == 'inventory':

                print(file)
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
