from src.connectz import *
import os


stripped_array = ['3 3 2', '1', '2', '1']

ones_first_col = ['7 6 4\n', '1\n', '2\n', '1\n', '2\n', '1\n', '2\n', '1\n']

subject = Connectz()
subject.run('tests/easy_test.txt')


class Test_Connectz:
    # def test_intify(self):
    #     assert subject.intify(stripped_array[1:]) == [1, 2, 1]

    def test_add_move(self):
        subject.board = [[], [], []]
        assert subject.add_move(1, 1) == [0, 0]

    def test_check_column(self):
        subject.board = [[1, 1], [2], []]
        assert subject.check_column([0, 1]) == 1
        assert subject.check_column([1, 0]) == -1

    def test_check_row_right(self):
        subject.board = [[2], [1], [1]]
        winning_move = [1, 0]
        losing_move = [0, 0]
        assert subject.check_row(winning_move, 'right') == 1
        assert subject.check_row(losing_move, 'right') == -1

    def test_check_row_left(self):
        subject.board = [[1, 2], [1], []]
        winning_move = [1, 0]
        losing_move = [0, 1]
        assert subject.check_row(winning_move, 'left') == 1
        assert subject.check_row(losing_move, 'left') == -1

    def test_diagonal_down_right(self):
        subject.z = 3
        subject.board = [[1, 2, 1], [2, 1, 2], [1]]
        winning_move = [0, 2]
        losing_move = [1, 2]
        assert subject.check_diagonal(winning_move, 'down', 'right') == 1
        assert subject.check_diagonal(losing_move, 'down', 'right') == -1

    def test_diagonal_down_left(self):
        subject.z = 3  # LOOK AT THIS AGAIN WHEN SORTED KEEP PLAYING ERR
        subject.board = [[1], [2, 1, 2], [1, 2, 1]]
        winning_move = [2, 2]
        losing_move = [1, 0]
        assert subject.check_diagonal(winning_move, 'down', 'left') == 1
        assert subject.check_diagonal(losing_move, 'down', 'left') == -1

    def test_diagonal_up_right(self):
        subject.z = 3
        subject.board = [[1, 1], [2, 1], [2, 2, 1]]
        winning_move = [0, 0]
        losing_move = [2, 0]
        assert subject.check_diagonal(winning_move, 'up', 'right') == 1
        assert subject.check_diagonal(losing_move, 'up', 'right') == -1

    def test_diagonal_up_left(self):
        subject.z = 3
        subject.board = [[1, 2, 1], [2, 1, 2], [1]]
        winning_move = [2, 0]
        losing_move = [0, 0]
        assert subject.check_diagonal(winning_move, 'up', 'left') == 1
        assert subject.check_diagonal(losing_move, 'up', 'left') == -1
