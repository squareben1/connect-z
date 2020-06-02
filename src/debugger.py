import sys

# f = open(sys.argv[1],"r")
# contents = f.readlines() #strip newline
# f.close()
# print(contents)

arr = ['3 3 2\n', '1\n', '2\n', '1\n']


def strip(array):
    stripped_arr = []
    for s in array:
        stripped_arr.append(s.rstrip("\n"))
    return stripped_arr

def intify(array):
    int_arr = []
    for i in array:
        int_arr.append(int(i))
    return int_arr

def arrayify(string):
    nums = string.split(' ')
    x = int(nums[0])  # width
    y = int(nums[1])  # height

    return [['-' for i in range(x)] for i in range(y)]

def add_moves(arr, arr2):
    return [['X']]
    # iterate over arr of arrs
    # add
