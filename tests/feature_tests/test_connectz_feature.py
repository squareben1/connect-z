from src.connectz import *

subject = Connectz()

class Test_Connectz_Features:
    def test_draw(self):
        assert subject.run('draw.txt') == 0

    def test_p1_win(self):
        assert subject.run('p1win.txt') == 1

    def test_reads_file_ok_p2_win(self):
        assert subject.run('p2win.txt') == 2

#  Error Tests
    def test_incomplete(self):
        assert subject.run('incomplete.txt') == 3

    def test_invalid_file(self):
        assert subject.run('invalid.txt') == 8

    def test_file_error(self):
        assert subject.run('notreal.txt') == 9

