from src.debugger import *

arr = ['3 3 2\n', '1\n', '2\n', '1\n']

def test_stripper_new_lines():
    assert strip(arr) == ['3 3 2', '1', '2', '1']