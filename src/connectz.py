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

    """
    In this solution columns are represented by arrays, rows by positions in them.
    Below game params = X = 3, Y = 3, Z = 2, moves = [1, 2, 1]
    [
      [1,1,_],  Column 1
      [2,_,_],  Column 2
      [_,_,_]   Column 3
    ] |  | |
      |  | └ ─ Row 3
      |  └ ─ Row 2
      └ ─	Row 1
    Player 1 wins
    """

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
            move_position = self.add_move(player, i)
            self.check_move(move_position)
            player = 2 if player == 1 else 1 # switch players after each move
        
    def add_move(self, player, move):
        self.board[move-1].append(player) # adds player to column
        return [move-1, len(self.board[move-1])-1] # [column_number, row_number]

    def check_move(self, move_position):
        # Check the different varitations of win
        # Game code returned, if null no game code applicable
        game_codes = []
        game_codes.append(self.check_column(move_position))
        game_codes.append(self.check_row(move_position, direction))

    def check_column(self, move_position):
        if len(self.board[move_position[0]]) < self.z: return -1 # guard clause if win is possible
        column = self.board[move_position[0]][-self.z:] 
        result = all(elem == column[0] for elem in column)
        return column[0] if result else -1

    def check_row(self, move_position, direction): 
        z_moves = []
        start_column = move_position[0]
        end_column = start_column + self.z
        move_row = move_position[1]
        if end_column + 1 > self.x: return -1  # guard: if not enough rows
        
        columns_to_check = self.board[start_column:end_column]
        
        for a in columns_to_check:
            if len(a) < (move_row + 1): return -1   # guard: if no value in row
            z_moves.append(a[move_row])

        result = all(elem == z_moves[0] for elem in z_moves)
        return z_moves[0] if result else -1

        
        
        

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