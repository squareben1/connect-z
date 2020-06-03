from src.connectz import *
# import os

arr = ['3 3 2\n', '1\n', '2\n', '1\n']
stripped_array = ['3 3 2', '1', '2', '1']
array_threes = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

subject = Connectz(arr) 

class Test_Connectz:
    def test_strip_new_lines(self):
        assert subject.strip(arr) == stripped_array

    def test_arrayify_ones(self):
        assert subject.arrayify('1 1') == ['1', '1']

    def test_arrayify_twos(self):
        assert subject.arrayify('2 2 2') == ['2', '2', '2']

    def test_intify(self):
        assert subject.intify(stripped_array[1:]) == [1, 2, 1]

    def test_inputs(self):
        assert subject.x == 3
        assert subject.y == 3
        assert subject.z == 2
        assert subject.moves == [1, 2, 1]