from src.debugger import *

arr = ['3 3 2\n', '1\n', '2\n', '1\n']
stripped_array = ['3 3 2', '1', '2', '1']
array_threes = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def test_stripper_new_lines():
    assert strip(arr) == stripped_array

def test_arrayify_ones():
    assert arrayify('1 1') == [['-']]

def test_arrayify_twos():
    assert arrayify('2 2') == [['-', '-'], ['-', '-']]

def test_arrayify_threes():
    assert arrayify('3 3') == [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def test_add_moves():
    print('stripped_array[1:]', stripped_array[1:])
    assert add_moves([['-']], ['1']) == [['X']]