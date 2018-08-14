import core
import disk


def customer(inv, customer_employee, rent_or_return):

    while input != 'q' or rent_or_return == 'R':

        print(inv)
        print()

        rental = int(input('Which would you like to rent today?(0, 5) '))
        print()
        if rental > 5:
            break

        name = input('What name would be on this rental? ')
        print()

        rental_length = input('How many months will you be renting? ')
        print()

        rent = core.Rental(name, [], rental_length, rent_or_return)
        item = inv[rental]
        rentals = rent.add_item(item)

        print('Thanks for your business.')
        print()

        print(rent)
        return rent
        break


def return_rental(inv, rent_or_return):
    while input != 'q' or rent_or_return == 'C':

        return_item = input('What rental would you like to close? ')
        print()

        customer = input('What was the name? ')
        print()

        length = input('How many months were you renting? ')
        print()

        print('Thank you for your business.')
        print()

        return_list = core.Rental(customer, [], length, rent_or_return)
        item = inv.return_item(return_item)
        rentals = return_list.add_item(item)

        for line in inv.properties:
            if return_item.lower() in line.name.lower():

                print(return_list.return_string())
                return return_list.return_string()

        break


def employee(customer_employee):
    while input != 'q':

        history = input(
            'Would you like to see the transaction [H]istory or the [I]nventory? '
        )
        print()

        if history == 'H':

            disk.employee()

        elif history == 'I':

            disk.print_inventory()
        break


def main():

    inv = disk.get_inventory()

    print('Welcome to my rental agency press "q" to quit at any time.')
    print()

    customer_employee = input('Are you a [C]ustomer or an [E]mployee? ')
    print()
    if customer_employee == 'C':
        rent_or_return = input(
            'Would you like to [R]ent or [C]lose a current rental? ')
        print()
        if rent_or_return == 'R':
            rent = customer(inv, customer_employee, rent_or_return)
            disk.write_to_log(rent)
        elif rent_or_return == 'C':
            return_log = return_rental(inv, rent_or_return)
            disk.write_to_log(return_log)
    elif customer_employee == 'E':
        employee(customer_employee)

    inventory = inv.update_stock()

    disk.give_inventory(inventory)


if __name__ == '__main__':
    main()
