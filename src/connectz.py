import sys

class Connectz:
    def __init__(self, array):
      self.string_array = self.strip(array) # strip new lines
      
      

    def strip(self, arr):
        return [s.rstrip("\n") for s in arr]

    def intify(self, array):
        return [int(i) for i in array]

    def arrayify(self, string):  # returns arr of Y arrs, each w/ X positions
        # nums = string.split(' ')
        # x = int(nums[0])  # width
        # y = int(nums[1])  # height

        return string.split(' ')


# new_game = Connectz()

# f = open(sys.argv[1], "r")
# contents = f.readlines()  # strip newline
# f.close()
# print(contents)
