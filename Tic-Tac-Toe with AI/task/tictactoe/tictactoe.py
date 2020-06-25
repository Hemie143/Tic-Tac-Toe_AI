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

    def print_grid(self):
        print("---------")
        for y in range(0, 3):
            # print(f'| {self.cells[y][0]} {self.cells[y][1]} {self.cells[y][2]} |')
            print(f'| {' '.join(cells[y])} |')
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

    def computer_play_easy(self):
        print('Making move level "easy"')
        found_cell = False
        while not found_cell:
            x = randint(0, 2)
            y = randint(0, 2)
            if self.cells[x][y] == " ":
                self.cells[x][y] = "O"
                found_cell = True

    def run(self):
        # Init
        self.print_grid()

        player = ["X", "O"]
        '''
        if field.count('X') == field.count('O'):
            turn = 0
        else:
            turn = 1
        '''

        # Loop start
        state = 'start'

        loop = 0

        while not self.end:
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
                # cells[3 - int(y)][int(x) - 1] = player[turn % 2]
                self.cells[3 - int(y)][int(x) - 1] = "X"
                self.print_grid()
                # turn += 1
                self.computer_play_easy()
                self.print_grid()

            self.get_state()
            if 'play' not in self.state:
                print(self.state)

            loop += 1
            if loop > 1:
                exit()


game = TicTacToe()
game.run()
