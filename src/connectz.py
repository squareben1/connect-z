import sys

class Connectz:
    def __init__(self, array):
      string_array = self.strip(array) # strip new lines
      arr = self.intify(self.arrayify(string_array[0])) # array of ints
      self.x = arr[0]
      self.y = arr[1]
      self.z = arr[2]
      self.moves = self.intify(string_array[1:])
      
    def strip(self, arr):
        return [s.rstrip("\n") for s in arr]

    def intify(self, array):
        return [int(i) for i in array]

    def arrayify(self, string):
        return string.split(' ')

    


# new_game = Connectz()

# f = open(sys.argv[1], "r")
# contents = f.readlines()  # strip newline
# f.close()
# print(contents)
