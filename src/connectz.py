import sys

class Connectz:
    def __init__(self, array):
      string_array = self.strip(array) # strip new lines
      arr = self.intify(self.arrayify(string_array[0])) # array of ints
      self.x = arr[0]
      self.y = arr[1]
      self.z = arr[2]
      self.moves = self.intify(string_array[1:])
      self.board = [[] for i in range(self.x)]

  # each array in board represents a column (Y height), board is array of columns i.e. X width
  # needs a check that move doesnt take len(column) over Y or len(board i.e. arr of arrs) over X
  # throw appropriate error in either case
      
    def strip(self, arr): #strip new lines
        return [s.rstrip("\n") for s in arr]

    def intify(self, array):
        return [int(i) for i in array]

    def arrayify(self, string):
        return string.split(' ')
    
    def play_game(self):
        player = 1
        for i in self.moves:
            # print(i)
            print(player)
            player = 2 if player == 1 else 1 # switch players after each move
            

    def add_move(self, player, move):
        print(self.board[move-1].append(player))

        return [move, len(self.board[move-1])-1] # [column_number, row_number]


    def check_game(self):
        print(self.board)
        

# new_game = Connectz()

# f = open(sys.argv[1], "r")
# contents = f.readlines()  # strip newline
# f.close()
# print(contents)


    # def split_players(self):
    #     p1 = []
    #     p2 = []
    #     for idx, i in enumerate(self.moves):
    #         if idx % 2 == 0:
    #             p1.append(i)
    #         else: 
    #             p2.append(i)
    #     return [p1, p2]