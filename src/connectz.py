import sys

class Connectz:
    def __init__(self, array):
      string_array = self.strip(array) # strip new lines
      arr = self.intify(self.arrayify(string_array[0])) # array of ints
      self.x = arr[0]
      self.y = arr[1]
      self.z = arr[2]
      self.moves = self.intify(string_array[1:])
  # want to remove these vars and just chain funcs?
      
    def strip(self, arr):
        return [s.rstrip("\n") for s in arr]

    def intify(self, array):
        return [int(i) for i in array]

    def arrayify(self, string):
        return string.split(' ')

    def split_players(self):
        p1 = []
        p2 = []
        for idx, i in enumerate(self.moves):
            if idx % 2 == 0:
                p1.append(i)
            else: 
                p2.append(i)
        return [p1, p2]

    def check_game(self):
        pass
# can check for either Z consecutive same or Z consecutive order (1,2,3,4)
    


# new_game = Connectz()

# f = open(sys.argv[1], "r")
# contents = f.readlines()  # strip newline
# f.close()
# print(contents)
