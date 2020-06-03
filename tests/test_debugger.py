from src.debugger import *

arr = ['3 3 2\n', '1\n', '2\n', '1\n']
stripped_array = ['3 3 2', '1', '2', '1']
array_twos = [['-', '-'], ['-', '-']]
array_threes = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def test_stripper_new_lines():
    assert strip(arr) == stripped_array

def test_arrayify_ones():
    assert arrayify('1 1') == [['-']]

def test_arrayify_twos():
    assert arrayify('2 2') == array_twos

def test_arrayify_threes():
    assert arrayify('3 3') == [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def test_intify():
    assert intify(stripped_array[1:]) == [1, 2, 1]

def test_add_moves_one():
    assert add_moves([['-']], [1]) == [['X']]

# def test_add_moves_two():
#     assert add_moves(array_twos, [1, 2]) == [['X', 'O'], ['-', '-']]
    