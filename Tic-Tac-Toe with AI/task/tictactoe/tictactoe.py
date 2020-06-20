from random import randint

class Player:

    def __init__(self, type, symbol):
        self.type = type
        self.symbol = symbol


class TicTacToe:

    valid_coords = ["1", "2", "3"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    def __init__(self):
        self.cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.state = 'play'
        self.end = False
        self.playerX = Player('', 'X')
        self.playerO = Player('', 'O')
        # self.symbol_map = {self.playerX: 'X', self.playerO: 'O'}

    def print_grid(self):
        print("---------")
        for y in range(0, 3):
            print(f'| {self.cells[y][0]} {self.cells[y][1]} {self.cells[y][2]} |')
        print("---------")

    def input_start_grid(self):
        field = input()
        for i in range(9):
            symbol = field[i]
            if symbol == '_':
                symbol = ' '
            self.cells[i // 3][i % 3] = symbol

    def get_state(self):
        empty_cell = any([cell == " " for row in self.cells for cell in row])
        x3 = self.cells[0] == ["X", "X", "X"] or self.cells[1] == ["X", "X", "X"] or self.cells[2] == ["X", "X", "X"] \
             or (self.cells[0][0] == "X" and self.cells[1][0] == "X" and self.cells[2][0] == "X") \
             or (self.cells[0][1] == "X" and self.cells[1][1] == "X" and self.cells[2][1] == "X") \
             or (self.cells[0][2] == "X" and self.cells[1][2] == "X" and self.cells[2][2] == "X") \
             or (self.cells[0][0] == "X" and self.cells[1][1] == "X" and self.cells[2][2] == "X") \
             or (self.cells[2][0] == "X" and self.cells[1][1] == "X" and self.cells[0][2] == "X")
        o3 = self.cells[0] == ["O", "O", "O"] or self.cells[1] == ["O", "O", "O"] or self.cells[2] == ["O", "O", "O"] \
             or (self.cells[0][0] == "O" and self.cells[1][0] == "O" and self.cells[2][0] == "O") \
             or (self.cells[0][1] == "O" and self.cells[1][1] == "O" and self.cells[2][1] == "O") \
             or (self.cells[0][2] == "O" and self.cells[1][2] == "O" and self.cells[2][2] == "O") \
             or (self.cells[0][0] == "O" and self.cells[1][1] == "O" and self.cells[2][2] == "O") \
             or (self.cells[2][0] == "O" and self.cells[1][1] == "O" and self.cells[0][2] == "O")

        if not x3 and not o3:
            if empty_cell:
                self.state = 'play'
            else:
                self.state = 'Draw'
                self.end = True
        elif x3:
            self.state = 'X wins'
            self.end = True
        elif o3:
            self.state = 'O wins'
            self.end = True

    @staticmethod
    def count_symbol(line, symbol):
        # returns 3, if 3 symbols
        # returns 2, if 2 symbols and 3rd cell is free
        # returns -1, if 2 symbols and 3rd cell is taken by opponent
        # returns 0 or 1 in other cases
        count = line.count(symbol)
        if count == 3:
            return 3
        elif count == 2:
            opposite_symbol = 'X' if symbol == 'O' else 'O'
            if line.count(opposite_symbol) == 1:
                return -1
            else:
                return 2
        else:
            return count
        return

    def check_row(self, row_number, symbol):
        row = self.cells[row_number]
        return self.count_symbol(row, symbol)

    def check_column(self, col_number, symbol):
        column = [r[col_number] for r in self.cells]
        return self.count_symbol(column, symbol)

    def check_diagonal(self, diagonal, symbol):
        if diagonal == 1:
            diag = [self.cells[i][i] for i in range(0, 3)]
        elif diagonal == 2:
            diag = [self.cells[i][2-i] for i in range(0, 3)]
        return self.count_symbol(diag, symbol)

    def fill_row(self, n, symbol, symbol_new):
        for i in range(0, 3):
            cell = self.cells[n][i]
            if cell != symbol and cell == ' ':
                self.cells[n][i] = symbol_new

    def fill_column(self, n, symbol, symbol_new):
        for i in range(0, 3):
            cell = self.cells[i][n]
            if cell != symbol and cell == ' ':
                self.cells[i][n] = symbol_new

    def fill_diagonal(self, n, symbol, symbol_new):
        if n == 1:
            for i in range(0, 3):
                cell = self.cells[i][i]
                if cell != symbol and cell == ' ':
                    self.cells[i][i] = symbol_new
        elif n == 2:
            for i in range(0, 3):
                cell = self.cells[i][2-i]
                if cell != symbol and cell == ' ':
                    self.cells[i][2-i] = symbol_new

    def play_computer_easy(self, player):
        print('Making move level "easy"')
        found_cell = False
        while not found_cell:
            x = randint(0, 2)
            y = randint(0, 2)
            if self.cells[x][y] == " ":
                self.cells[x][y] = player.symbol
                found_cell = True

    def play_computer_medium(self, player):
        print('Making move level "medium"')
        found_cell = False
        # Win in one move ?
        for i in range(0, 3):
            if self.check_row(i, player.symbol) == 2:
                self.fill_row(i, player.symbol, player.symbol)
                found_cell = True
                break
        if not found_cell:
            for i in range(0, 3):
                if self.check_column(i, player.symbol) == 2:
                    self.fill_column(i, player.symbol, player.symbol)
                    found_cell = True
                    break
        if not found_cell:
            for i in range(1, 2):
                if self.check_diagonal(i, player.symbol) == 2:
                    self.fill_diagonal(i, player.symbol, player.symbol)
                    found_cell = True
                    break
        # Check opponent win in one move
        opposite_symbol = 'X' if player.symbol == 'O' else 'O'
        if not found_cell:
            for i in range(0, 3):
                if self.check_row(i, player.symbol) == 2:
                    self.fill_row(i, player.symbol, opposite_symbol)
                    found_cell = True
                    break
        if not found_cell:
            for i in range(0, 3):
                if self.check_column(i, player.symbol) == 2:
                    self.fill_column(i, player.symbol, opposite_symbol)
                    found_cell = True
                    break
        if not found_cell:
            for i in range(1, 2):
                if self.check_diagonal(i, player.symbol) == 2:
                    self.fill_diagonal(i, player.symbol, opposite_symbol)
                    found_cell = True
                    break
        while not found_cell:
            x = randint(0, 2)
            y = randint(0, 2)
            if self.cells[x][y] == " ":
                self.cells[x][y] = player.symbol
                found_cell = True

    def play_user(self, player):
        while True:
            move = input("Enter the coordinates:")
            if " " not in move:
                print("You should enter numbers!")
                continue
            else:
                x, y = move.split()
            if not x.isnumeric() and not y.isnumeric():
                print("You should enter numbers!")
            elif x not in self.valid_coords or y not in self.valid_coords:
                print("Coordinates should be from 1 to 3!")
            elif self.cells[3 - int(y)][int(x) - 1] in "XO":
                print("This cell is occupied! Choose another one!")
            else:
                # Turns
                self.cells[3 - int(y)][int(x) - 1] = player.symbol
                break

    def play(self):
        while not self.end:
            for player in [self.playerX, self.playerO]:
                if player.type == 'easy':
                    self.play_computer_easy(player)
                if player.type == 'medium':
                    self.play_computer_medium(player)
                elif player.type == 'user':
                    self.play_user(player)
                self.print_grid()
                self.get_state()
                if 'play' not in self.state:
                    print(self.state)
                    break

    def run_menu(self):
        while True:
            print('Input command:')
            command = input()
            if command == 'exit':
                exit()
            if command.startswith('start') and command.count(' ') == 2:
                _, typeX, typeO = command.split(' ')
                self.playerX.type = typeX
                self.playerO.type = typeO
                self.play()
            else:
                print('Bad parameters!')
            # exit()


game = TicTacToe()
game.run_menu()
