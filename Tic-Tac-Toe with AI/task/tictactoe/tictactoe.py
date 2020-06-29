from random import randint

class Player:

    def __init__(self, level, symbol):
        self.level = level
        self.symbol = symbol


class UserPlayer(Player):

    valid_coords = ["1", "2", "3"]

    def play(self, grid):
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
            elif grid[3 - int(y)][int(x) - 1] in "XO":
                print("This cell is occupied! Choose another one!")
            else:
                # Turns
                # cells[3 - int(y)][int(x) - 1] = player[turn % 2]
                grid[3 - int(y)][int(x) - 1] = "X"
                break

class AIEasyPlayer(Player):

    def play(self, grid):
        print('Making move level "easy"')
        found_cell = False
        while not found_cell:
            x = randint(0, 2)
            y = randint(0, 2)
            if grid[x][y] == " ":
                grid[x][y] = self.symbol
                found_cell = True


class TicTacToe:

    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    lines = [([0, 0], [0, 1], [0, 2]), ([1, 0], [1, 1], [1, 2]), ([2, 0], [2, 1], [2, 2]),
             ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 1], [2, 1]), ([0, 2], [2, 2], [2, 2]),
             ([0, 0], [1, 1], [2, 1]), ([2, 0], [1, 1], [0, 2])
             ]

    def __init__(self):
        self.state = 'play'
        self.win = False
        self.playerX = None
        self.playerO = None
        self.init_grid()

    def init_grid(self):
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def print_grid(self):
        print("---------")
        for y in range(0, 3):
            grid_line = ' '.join(self.grid[y])
            print(f'| {grid_line} |')
        print("---------")

    def input_start_grid(self):
        field = input()
        for i in range(9):
            symbol = field[i]
            if symbol == '_':
                symbol = ' '
            self.grid[i // 3][i % 3] = symbol

    def get_state(self):
        empty_cell = any([cell == " " for row in self.grid for cell in row])
        x3, o3 = False, False
        for coords in self.lines:
            line = [self.grid[x][y] for x, y in coords]
            x3 = x3 or all([c == 'X' for c in line])
            o3 = o3 or all([c == 'X' for c in line])
        if not x3 and not o3:
            if empty_cell:
                self.state = 'play'
            else:
                self.state = 'Draw'
                self.win = True
        elif x3:
            self.state = 'X wins'
            self.win = True
        elif o3:
            self.state = 'O wins'
            self.win = True

    @staticmethod
    def get_player(level, symbol):
        if level == 'user':
            return UserPlayer(level, symbol)
        elif level == 'easy':
            return AIEasyPlayer(level, symbol)

    def run(self):
        self.print_grid()
        while not self.win:
            for player in [self.playerX, self.playerO]:
                player.play(self.grid)
                self.print_grid()
                self.get_state()
                if 'play' not in self.state:
                    print(self.state)
                if self.win:
                    break

    def run_menu(self):
        while True:
            print('Input command:')
            command = input()
            if command == 'exit':
                exit()
            if command.startswith('start') and command.count(' ') == 2:
                _, levelX, levelO = command.split(' ')
                self.playerX = self.get_player(levelX, 'X')
                self.playerO = self.get_player(levelO, 'O')
                self.init_grid()
                self.run()
            else:
                print('Bad parameters!')
            exit()

game = TicTacToe()
# game.playerX = game.get_player('user', 'X')
# game.playerO = game.get_player('easy', 'O')
game.run_menu()
