from src.format import *

easy_arr = ['3 3 2\n', '1\n', '2\n', '1\n']
stripped_array = ['3 3 2', '1', '2', '1']

subject = Format()

class Test_Format:
    def test_strip_new_lines(self):
        assert subject.strip(easy_arr) == stripped_array