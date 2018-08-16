import core
import disk
import time


def customer(inv, customer_employee, rent_or_return):

    while True:

        print(inv)
        print()
        rental = input(
            'Which would you like to rent today?(First letter of rental) ')
        print()
        time.sleep(.5)

        name = input('What name would be on this rental? ')
        print()
        time.sleep(.5)
        while True:
            rental_length = input('How many months will you be renting? ')
            print()
            if rental_length.isdigit() == True:
                print('One moment please.......')
                print()
                time.sleep(1)
                rent = core.Rental(name, [], rental_length, rent_or_return)
                item = inv[rental]
                rentals = rent.add_item(item)

                print('Thanks for your business.')
                print()

                print(rent)
                return rent
            else:
                print('Please enter a number.')
                print()
        else:
            print('Invalid Response')


def rent_or_return(inv, rent_or_return):

    customer = input('What\'s your name? ')
    print()
    time.sleep(.5)
    while True:
        return_item = input(
            'okay ' + customer +
            ' what rental would you like to close?(First letter of rental) ')
        print()
        time.sleep(.5)
        while True:
            length = input('How many months were you renting? ')
            print()
            if length.isdigit() == True:

                print('One moment please.........')
                print()
                time.sleep(1)
                print('Thank you for your business.')
                print()

                return_list = core.Rental(customer, [], length, rent_or_return)
                item = inv.return_item(return_item)
                rentals = return_list.add_item(item)

                print(return_list.return_string())
                return return_list

            else:
                print('Please enter a number.')
                print()


def employee(customer_employee):
    while True:

        history = input(
            'Would you like to see the transaction [H]istory or the [I]nventory? '
        )
        print()

        if history == 'H'.lower() or 'H':
            time.sleep(1)
            print(disk.employee())
            print('Total: {}'.format(disk.revenue()))
            break

        elif history == 'I'.lower() or 'I':
            time.sleep(1)
            print(disk.print_inventory())
            break
        else:
            print('Please select History or Inventory.')
            print()


def main():

    inv = disk.get_inventory()
    print('Welcome to my rental agency press "q" to quit at any time.')
    print()
    while True:
        customer_employee = input('Are you a [C]ustomer or an [E]mployee? ')
        print()
        if customer_employee == 'C'.lower() or 'C':
            time.sleep(.5)
            while True:
                rent_or_return = input(
                    'Would you like to [R]ent or [C]lose a current rental? ')
                print()
                if rent_or_return == 'R'.lower() or 'R':
                    rent = customer(inv, customer_employee, rent_or_return)
                    disk.write_to_log(rent)
                    break
                elif rent_or_return == 'C'.lower() or 'C':
                    return_list = return_rental(inv, rent_or_return)
                    disk.write_to_log_return(return_list)
                    break
                elif rent_or_return == 'Q'.lower() or 'Q':
                    break
            break
        elif customer_employee == 'E'.lower() or 'E':
            employee(customer_employee)

            break

    inventory = inv.update_stock()

    disk.give_inventory(inventory)


if __name__ == '__main__':
    main()
