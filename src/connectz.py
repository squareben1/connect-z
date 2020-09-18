import sys
import re


class InputFormatter:
    def strip_new_lines(self, arr):
        return [s.rstrip("\n") for s in arr]

    def arrayify(self, string):
        return string.split(' ')

    def intify(self, array):
        return [int(i) for i in array]


class Connectz:

    def run(self, file_path=''):
        self.formatter = InputFormatter()

        if file_path == '':
            return 'connectz.py: Provide one input file'
        result = self.read_file(file_path)
        if result == 9 or result == 8:
            return result

        string_array = self.formatter.strip_new_lines(
            result)  # strip new lines
        arr = self.formatter.intify(self.formatter.arrayify(
            string_array[0]))  # array of ints
        self.x = arr[0]
        self.y = arr[1]
        self.line_length = arr[2]
        self.moves = self.formatter.intify(string_array[1:])
        self.board = [[] for i in range(self.x)]
        self.won = False

        if self.line_length > self.x or self.line_length > self.y:  # if illegal game
            return 7

        return self.play_game()

    def read_file(self, file_path):
        try:
            f = open(file_path, "r")
        except FileNotFoundError:
            return 9

        f = open(file_path, "r")
        contents = f.readlines()  # strip newline
        f.close()

        file_string = ''.join(contents)
        pattern = re.compile(r'\d \d \d\n(?:\d\n)+\d\Z')

        match = pattern.match(file_string)
        if match == None:
            return 8

        return contents

    def play_game(self):
        player = 1  # track turn
        max_moves = self.x * self.y
        number_of_moves = len(self.moves)

        for i in range(number_of_moves):
            move = self.moves.pop(0)
            move_position = self.add_move(player, move)
            if isinstance(move_position, int):
                return move_position
            result = self.check_move(move_position)
            if result:
                if len(self.moves) > 0:  # check if there are still moves in moves array after game won
                    return 4
                self.won = True
                return result
            elif max_moves == i + 1:  # if draw
                return 0
            player = 2 if player == 1 else 1  # switch players after each move

        # no more moves, game incomplete:
        return 3

    def add_move(self, player, move):
        if move > self.x or move < 1:  # if illegal column
            return 6
        elif len(self.board[move-1]) >= self.y:  # if illegal row
            return 5
        self.board[move-1].append(player)  # adds player to column
        # [column_number, row_number]
        return [move-1, len(self.board[move-1])-1]

    def check_move(self, move_position):
        # Check the different varitations of win, -1 pushed to game_codes unless win, 1 pushed if win
        game_codes = []
        game_codes.append(self.check_column(move_position))
        game_codes.append(self.check_row(move_position, 'right'))
        game_codes.append(self.check_row(move_position, 'left'))
        game_codes.append(self.check_diagonal(move_position, 'up', 'left'))
        game_codes.append(self.check_diagonal(move_position, 'up', 'right'))
        game_codes.append(self.check_diagonal(move_position, 'down', 'left'))
        game_codes.append(self.check_diagonal(move_position, 'down', 'right'))

        win_result = list(filter(lambda a: a != -1, game_codes))

        if win_result:
            self.won = True
            return win_result[0]

    def check_column(self, move_position):
        if len(self.board[move_position[0]]) < self.line_length:
            return -1  # guard: if win is impossible bc column is < Z
        column = self.board[move_position[0]
                            ][-self.line_length:]  # get Z elems in col
        result = all(elem == column[0] for elem in column)  # check all same
        return column[0] if result else -1

    def check_row(self, move_position, direction):
        z_moves = []
        row_height = move_position[1]
        if direction == 'right':
            start_column = move_position[0]
            end_column = start_column + self.line_length - 1
            if end_column > self.x:
                return -1  # guard: if not enough rows to right HERE
        else:
            start_column = move_position[0] - self.line_length + 1
            end_column = move_position[0]
            if start_column < 0:
                return -1  # guard: if not enough rows to left

        columns_to_check = self.board[start_column:end_column + 1]

        for a in columns_to_check:
            if len(a) < (row_height + 1):
                return -1  # guard: if no value in row
            z_moves.append(a[row_height])

        return self.check_elems(z_moves)

    def check_elems(self, moves):
      # result true if all element in z_moves are the same
        result = all(elem == moves[0] for elem in moves)
        return moves[0] if result else -1

    def check_diagonal(self, move_position, vertical, horizontal):
        z_moves = []
        starting_column = move_position[0]
        row_height = move_position[1]
        vertical_iterator = 1 if vertical == 'up' else -1
        horiztonal_iterator = 1 if horizontal == 'right' else -1

        # get columns and check horizontal range
        if horizontal == 'right':
            if (move_position[0] + self.line_length) > self.x:
                return -1  # guard: if not enough rows to right
        else:
            if (move_position[0] - self.line_length + 1) < 0:
                return -1  # guard: if not enough rows to left

        # iterate diagonally to get values to check
        for i in range(self.line_length):
            column_loc = starting_column + (i * horiztonal_iterator)
            row_loc = row_height + (i * vertical_iterator)
            if len(self.board[column_loc]) < (row_loc + 1) or row_loc < 0:
                return -1  # guard: if no value in row exit
            next_value = self.board[column_loc][row_loc]
            z_moves.append(next_value)

        # result true if all element in z_moves are the same
        return self.check_elems(z_moves)
