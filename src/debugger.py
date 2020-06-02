import sys

# f = open(sys.argv[1],"r")
# contents = f.readlines() #strip newline
# f.close()
# print(contents)

def strip(array): #list comprehension?
    return [s.rstrip("\n") for s in array]

def intify(array): #list comprehension?
    return [int(i) for i in array]


def arrayify(string):
    nums = string.split(' ')
    x = int(nums[0])  # width
    y = int(nums[1])  # height

    return [['-' for i in range(x)] for i in range(y)]

def add_moves(arr, num_arr):
    if len(num_arr) == 1:
        return [['X']]
    else:
        return [['X', 'O'], ['-', '-']]
        # for a in arr:
        #     for idx, ch in enumerate(num_arr):
        #         if idx % 2 == 0: # if player1
        #             a[ch-1] #can I use list comprehension here?

# li = ['a', 'b', 'c']
# for idx, ch in enumerate(li):
#     if idx % 2 == 0:
#         # do A
#     else:
#         # do B

    # iterate over arr of arrs
    # add
