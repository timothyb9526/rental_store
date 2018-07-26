import shell
from bcca.test import (with_inputs, should_print, fake_file)


@with_inputs('Cabin', 'Large cabin')
@should_print
def get_item(output):
    shell.main()
    assert output == """ 
"""
