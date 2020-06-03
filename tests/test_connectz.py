from src.connectz import *
# import os

easy_arr = ['3 3 2\n', '1\n', '2\n', '1\n']
stripped_array = ['3 3 2', '1', '2', '1']

ones_first_col = ['7 6 4\n', '1\n', '2\n', '1\n', '2\n', '1\n', '2\n', '1\n']

subject = Connectz(easy_arr)


class Test_Connectz:
    def test_strip_new_lines(self):
        assert subject.strip(easy_arr) == stripped_array

    def test_arrayify_ones(self):
        assert subject.arrayify('1 1') == ['1', '1']

    def test_arrayify_twos(self):
        assert subject.arrayify('2 2 2') == ['2', '2', '2']

    def test_intify(self):
        assert subject.intify(stripped_array[1:]) == [1, 2, 1]

    def test_easy_inputs(self):
        assert subject.x == 3
        assert subject.y == 3
        assert subject.z == 2
        assert subject.moves == [1, 2, 1]

    # def test_easy_logic(self):
    #     assert subject.play_game() == 1

    def test_add_move(self):
        assert subject.add_move(1, 1) == [0, 0]

    def test_check_column(self):
        subject.board = [[1, 1], [2], []]
        assert subject.check_column([0, 1]) == 1
        assert subject.check_column([1, 0]) == -1

    def test_check_row(self):
        subject.board = [[1, 2], [1], []]
        winning_move = [1, 0]
        assert subject.check_row(winning_move, 'right') == -1
        
        losing_move = [0, 1]
