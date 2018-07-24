import shell
from bcca.test import (with_inputs, should_print, fake_file)


@with_inputs('Book', 'Lonesome Dove')
@should_print
def get_item(output):
    shell.main()
    assert output == """ 
Category: Book 
Item name: Lonesome Dove 
days rented: 2 
rent price: $10.00 
replacement value: $2.00
"""
