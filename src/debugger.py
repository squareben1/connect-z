import sys

# f = open(sys.argv[1],"r")
# contents = f.readlines() #strip newline
# f.close()
# print(contents)


def strip(array):
    return [s.rstrip("\n") for s in array]


def intify(array):
    return [int(i) for i in array]


def arrayify(string):  # returns arr of Y arrs, each w/ X positions
    nums = string.split(' ')
    x = int(nums[0])  # width
    y = int(nums[1])  # height

    return [['-' for i in range(x)] for i in range(y)]


def add_moves(arr, num_arr):
    if len(num_arr) == 1:
        return [['X']]
        return []
    else:
        [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
        # return [['X', 'O'], ['-', '-']]
        print('arr:', arr)
        for a in arr:
            # return [a[idx] = 'X' if idx % 2 == 0 else a[idx] = 'O' for idx, i in enumerate(num_arr)]
            # return ['X' if idx % 2 == 0 else 'O' for idx, i in enumerate(num_arr)]
            for idx, i in enumerate(num_arr): #should only do once? certainly not once each number
                print(idx)
                if idx % 2 == 0: # if player1
                    a[idx] = 'X'
                else: 
                    a[idx] = 'O'
        return arr
            
            # HAVE I OVER COMPLICATED THIS WITH ARRAYS?? WHY NOT JUST STRINGS??? XOX
            # but then would list comprehension work ? 
         

# li = ['a', 'b', 'c']
# for idx, ch in enumerate(li):
#     if idx % 2 == 0:
#         # do A
#     else:
#         # do B

    # iterate over arr of arrs
    # add
