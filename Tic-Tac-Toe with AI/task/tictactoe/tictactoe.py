from random import randint


def print_state(cells):
    print("---------")
    for y in range(0, 3):
        print(f'| {cells[y][0]} {cells[y][1]} {cells[y][2]} |')
    print("---------")


def input_start_grid():
    grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    field = input()
    for i in range(9):
        symbol = field[i]
        if symbol == '_':
            symbol = ' '
        grid[i // 3][i % 3] = symbol
    return grid


def get_state():
    empty_cell = any([cell == " " for row in cells for cell in row])
    x3 = cells[0] == ["X", "X", "X"] or cells[1] == ["X", "X", "X"] or cells[2] == ["X", "X", "X"] \
         or (cells[0][0] == "X" and cells[1][0] == "X" and cells[2][0] == "X") \
         or (cells[0][1] == "X" and cells[1][1] == "X" and cells[2][1] == "X") \
         or (cells[0][2] == "X" and cells[1][2] == "X" and cells[2][2] == "X") \
         or (cells[0][0] == "X" and cells[1][1] == "X" and cells[2][2] == "X") \
         or (cells[2][0] == "X" and cells[1][1] == "X" and cells[0][2] == "X")
    o3 = cells[0] == ["O", "O", "O"] or cells[1] == ["O", "O", "O"] or cells[2] == ["O", "O", "O"] \
         or (cells[0][0] == "O" and cells[1][0] == "O" and cells[2][0] == "O") \
         or (cells[0][1] == "O" and cells[1][1] == "O" and cells[2][1] == "O") \
         or (cells[0][2] == "O" and cells[1][2] == "O" and cells[2][2] == "O") \
         or (cells[0][0] == "O" and cells[1][1] == "O" and cells[2][2] == "O") \
         or (cells[2][0] == "O" and cells[1][1] == "O" and cells[0][2] == "O")

    if not x3 and not o3:
        if empty_cell:
            return 'Next'
        else:
            return 'Draw'
    elif x3:
        return 'X wins'
    elif o3:
        return 'O wins'


def computer_play_easy():
    print('Making move level "easy"')
    found_cell = False
    while not found_cell:
        x = randint(0, 2)
        y = randint(0, 2)
        if cells[x][y] == " ":
            cells[x][y] = "O"
            found_cell = True


# Init
valid_coords = ["1", "2", "3"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print_state(cells)

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

while not 'wins' in state:
    move = input("Enter the coordinates:")
    if " " not in move:
        print("You should enter numbers!")
        continue
    else:
        x, y = move.split()
    if not x.isnumeric() and not y.isnumeric():
        print("You should enter numbers!")
    elif x not in valid_coords or y not in valid_coords:
        print("Coordinates should be from 1 to 3!")
    elif cells[3 - int(y)][int(x) - 1] in "XO":
        print("This cell is occupied! Choose another one!")
    else:
        # Turns
        # cells[3 - int(y)][int(x) - 1] = player[turn % 2]
        cells[3 - int(y)][int(x) - 1] = "X"
        print_state(cells)
        # turn += 1
        computer_play_easy()
        print_state(cells)

    state = get_state()
    if state != 'Next':
        print(state)

    loop += 1
    if loop > 9:
        exit()
