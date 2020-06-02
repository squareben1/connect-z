from src.debugger import *

arr = ['3 3 2\n', '1\n', '2\n', '1\n']
stripped_array = ['3 3 2', '1', '2', '1']

def test_stripper_new_lines():
    assert strip(arr) == stripped_array

def test_arrayify():
    assert arrayify(['1 1']) == [['-']]