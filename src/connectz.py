import sys


class Connectz:
    def __init__(self, file_path):
        array = self.read_file(file_path)

        string_array = self.strip(array)  # strip new lines
        arr = self.intify(self.arrayify(string_array[0]))  # array of ints
        self.x = arr[0]
        self.y = arr[1]
        self.z = arr[2]
        self.moves = self.intify(string_array[1:])
        self.board = [[] for i in range(self.x)]

    def read_file(self, file_path):
      f = open(file_path, "r")
      contents = f.readlines()  # strip newline
      f.close()
      
      return contents

    """
    In this solution columns are represented by arrays, rows by positions in them.
    Below game params = X = 3, Y = 3, Z = 2, moves = [1, 2, 1]
    [
      [1,1,_], ─ Column 1
      [2,_,_], ─ Column 2
      [_,_,_]  ─ Column 3
    ]  | | |
       | | └ ─ Row 3
       | └ ─ Row 2
       └ ─	Row 1
    Player 1 wins
    """

  # each array in board represents a column (Y height), board is array of columns i.e. X width
  # needs a check that move doesnt take len(column) over Y or len(board i.e. arr of arrs) over X
  # throw appropriate error in either case

    def strip(self, arr):  # strip new lines
        return [s.rstrip("\n") for s in arr]

    def intify(self, array):
        return [int(i) for i in array]

    def arrayify(self, string):
        return string.split(' ')

    def play_game(self):
        player = 1
        print(self.moves)
        for i in self.moves:
            move_position = self.add_move(player, i)
            result = self.check_move(move_position)
            if result: return result
            player = 2 if player == 1 else 1  # switch players after each move

    def add_move(self, player, move):
        self.board[move-1].append(player)  # adds player to column
        # [column_number, row_number]
        return [move-1, len(self.board[move-1])-1]

    def check_move(self, move_position):
        # Check the different varitations of win
        # Game code returned, if null no game code applicable
        game_codes = []
        game_codes.append(self.check_column(move_position))
        game_codes.append(self.check_row(move_position, 'right'))
        game_codes.append(self.check_row(move_position, 'left'))
        game_codes.append(self.check_diagonal(move_position, 'up', 'left'))
        game_codes.append(self.check_diagonal(move_position, 'up', 'right'))
        game_codes.append(self.check_diagonal(move_position, 'down', 'left'))
        game_codes.append(self.check_diagonal(move_position, 'down', 'right'))
        result = list(filter(lambda a: a != -1, game_codes))
        if result: return result[0]

    def check_column(self, move_position):
        if len(self.board[move_position[0]]) < self.z:
            return -1  # guard: if win is possible
        column = self.board[move_position[0]][-self.z:]
        result = all(elem == column[0] for elem in column)
        return column[0] if result else -1

    def check_row(self, move_position, direction):
        z_moves = []
        row_height = move_position[1]
        if direction == 'right':
            start_column = move_position[0]
            end_column = start_column + self.z - 1
            if end_column > self.x:
                return -1  # guard: if not enough rows to right
        else:
            start_column = move_position[0] - self.z + 1
            end_column = move_position[0]
            if start_column < 0:
                return -1  # guard: if not enough rows to left

        columns_to_check = self.board[start_column:end_column + 1]

        for a in columns_to_check:
            if len(a) < (row_height + 1):
                return -1  # guard: if no value in row
            z_moves.append(a[row_height])

        # result true if all element in z_moves are the same
        result = all(elem == z_moves[0] for elem in z_moves)
        return z_moves[0] if result else -1

    def check_diagonal(self, move_position, vertical, horizontal):
        z_moves = []
        starting_column = move_position[0]
        row_height = move_position[1]
        vertical_iterator = 1 if vertical == 'up' else -1
        horiztonal_iterator = 1 if horizontal == 'right' else -1

        # get columns and check horizontal range
        if horizontal == 'right':
            if (move_position[0] + self.z) > self.x:
                return -1  # guard: if not enough rows to right
        else:
            if (move_position[0] - self.z + 1) < 0:
                return -1  # guard: if not enough rows to left

        # iterate diagonally to get values to check
        for i in range(self.z):
            column_loc = starting_column + (i * horiztonal_iterator)
            row_loc = row_height + (i * vertical_iterator)
            if len(self.board[column_loc]) < (row_loc + 1) or row_loc < 0:
                return -1  # guard: if no value in row exit
            next_value = self.board[column_loc][row_loc]
            z_moves.append(next_value)

        # result true if all element in z_moves are the same
        result = all(elem == z_moves[0] for elem in z_moves)
        return z_moves[0] if result else -1



# f = open(sys.argv[1], "r")
# contents = f.readlines()  # strip newline
# f.close()
# print(contents)

# new_game = Connectz(contents)
# result_code = new_game.play_game()
# print(result_code)
