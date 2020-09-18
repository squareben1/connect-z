from src.connectz import InputFormatter

easy_arr = ['3 3 2\n', '1\n', '2\n', '1\n']
stripped_array = ['3 3 2', '1', '2', '1']

subject = InputFormatter()


class Test_Format:
    def test_strip_new_lines(self):
        assert subject.strip_new_lines(easy_arr) == stripped_array

    def test_arrayify_ones(self):
        assert subject.arrayify('1 1') == ['1', '1']

    # def test_arrayify_twos(self):
    #     assert subject.arrayify('2 2 2') == ['2', '2', '2']

    # def test_intify(self):
    #     assert subject.intify(stripped_array[1:]) == [1, 2, 1]
