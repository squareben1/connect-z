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


def arrayify(array):
    strings = array[0].split(' ')
    x = int(strings[0]) #width
    y = int(strings[1]) #height

    return [['-' for i in range(x)] for i in range(y)]



