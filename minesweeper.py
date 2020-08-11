# Author: Mihai Ion

import random
import re
from math import floor

# setting boundaries for size of grid
max_size = 12
min_size = 4
mines_ratio = 0.1

COORD_RE = re.compile(r"^([#\?])?\s*([a-z])\s*[,.:]?\s*([a-z])$",re.IGNORECASE)

# getting input from player
while True:
    s1 = int(input("Enter square-grid dimension " + str(min_size) + "-" + str(max_size) + ": "))
    if max_size >= s1 >= min_size:
        break

# total number of mines on the board
mines = floor(s1**2 * mines_ratio)


def minesweeper_grid(dimensions):
    """creating a game board with dimensions"""

    # using dictionary to store all of values and if visited values
    game_grid = dict()
    for i in range(dimensions):
        for e in range(dimensions):
            game_grid[i, e] = [0, False]

    return game_grid


def min_adjc(v):
    return max(v - 1, 0)


def max_adjc(v, size):
    return min(v + 2, size)


def range_adjc(v, size):
    return range(min_adjc(v), max_adjc(v, size))


def list_adjc(size, x, y):
    return [(i, j) for i in range_adjc(x, size) for j in range_adjc(y, size)]


def format_cell(val, showall):
    """prints out the table with values hidden until
    either clicked or game ended"""

    v = " "
    if showall:
        if val[0] == 0:
            v = str(' ')
        else:
            v = str(val[0])
    elif val[1] is False:
        v = "."
    elif val[1] is True:
        if val[0] == 0:
            v = str(' ')
        elif type(val[0]) == int:
            v = str(val[0])
        elif val[0] == 'X':
            v = 'X'

    return v


def insert_mines(game_grid, dimensions, bombs):
    """insert mines with preset mines to dimensions ratio"""

    for num in range(bombs):
        while True:
            x = random.randrange(0, dimensions - 1)
            y = random.randrange(0, dimensions - 1)
            if game_grid[y,x][0] != 'X':
                game_grid[y,x][0] = 'X'
                break

        if (0 < x < dimensions - 1) and (0 < y < dimensions - 1):
            if game_grid[y,x+1][0] != 'X': # center right
                game_grid[y,x+1][0] += 1
            if game_grid[y+1,x+1][0] != 'X':  # right bottom
                game_grid[y+1,x+1][0] += 1
            if game_grid[y+1,x][0] != 'X':
                game_grid[y+1,x][0] += 1
            if game_grid[y+1,x-1][0] != 'X':
                game_grid[y+1,x-1][0] += 1
            if game_grid[y,x-1][0] != 'X':
                game_grid[y,x-1][0] += 1
            if game_grid[y-1,x-1][0] != 'X':
                game_grid[y-1,x-1][0] += 1
            if game_grid[y-1,x][0] != 'X':
                game_grid[y-1,x][0] += 1
            if game_grid[y-1,x+1][0] != 'X':
                game_grid[y-1,x+1][0] += 1

        elif y == 0 and 0 < x < dimensions - 1:
            if game_grid[y,x+1][0] != 'X':
                game_grid[y,x+1][0] += 1
            if game_grid[y+1,x+1][0] != 'X':
                game_grid[y+1,x+1][0] += 1
            if game_grid[y+1,x][0] != 'X':
                game_grid[y+1,x][0] += 1
            if game_grid[y+1,x-1][0] != 'X':
                game_grid[y+1,x-1][0] += 1
            if game_grid[y,x-1][0] != 'X':
                game_grid[y,x-1][0] += 1

        elif y == dimensions-1 and 0 < x < dimensions - 1:
            if game_grid[y,x-1][0] != 'X':
                game_grid[y,x-1][0] += 1
            if game_grid[y-1,x-1][0] != 'X':
                game_grid[y-1,x-1][0] += 1
            if game_grid[y-1,x][0] != 'X':
                game_grid[y-1,x][0] += 1
            if game_grid[y,x+1][0] != 'X':
                game_grid[y,x+1][0] += 1
            if game_grid[y-1,x+1][0] != 'X':
                game_grid[y-1,x+1][0] += 1

        elif 0 < y < dimensions - 1 and x == 0:
            if game_grid[y-1,x][0] != 'X':
                game_grid[y-1,x][0] += 1
            if game_grid[y-1,x+1][0] != 'X':
                game_grid[y-1,x+1][0] += 1
            if game_grid[y,x+1][0] != 'X':
                game_grid[y,x+1][0] += 1
            if game_grid[y+1,x+1][0] != 'X':
                game_grid[y+1,x+1][0] += 1
            if game_grid[y+1,x][0] != 'X':
                game_grid[y+1,x][0] += 1

        elif 0 < y < dimensions - 1 and x == dimensions - 1:
            if game_grid[y-1,x][0] != 'X':
                game_grid[y-1,x][0] += 1
            if game_grid[y-1,x-1][0] != 'X':
                game_grid[y-1,x-1][0] += 1
            if game_grid[y,x-1][0] != 'X':
                game_grid[y,x-1][0] += 1
            if game_grid[y+1,x+1][0] != 'X':
                game_grid[y+1,x+1][0] += 1
            if game_grid[y+1,x][0] != 'X':
                game_grid[y+1,x][0] += 1

        elif y == 0 and x == 0:
            if game_grid[y+1,x][0] != 'X':
                game_grid[y+1,x][0] += 1
            if game_grid[y+1,x+1][0] != 'X':
                game_grid[y+1,x+1][0] += 1
            if game_grid[y,x+1][0] != 'X':
                game_grid[y,x+1][0] += 1

        elif y == 0 and x == dimensions-1:
            if game_grid[y+1,x][0] != 'X':
                game_grid[y+1,x][0] += 1
            if game_grid[y+1,x-1][0] != 'X':
                game_grid[y+1,x-1][0] += 1
            if game_grid[y,x-1][0] != 'X':
                game_grid[y,x-1][0] += 1

        elif y == dimensions-1 and x == dimensions-1:
            if game_grid[y-1,x][0] != 'X':
                game_grid[y-1,x][0] += 1
            if game_grid[y-1,x-1][0] != 'X':
                game_grid[y-1,x-1][0] += 1
            if game_grid[y,x-1][0] != 'X':
                game_grid[y,x-1][0] += 1

        elif y == dimensions-1 and x == 0:
            if game_grid[y-1,x][0] != 'X':
                game_grid[y-1,x][0] += 1
            if game_grid[y-1,x+1][0] != 'X':
                game_grid[y-1,x+1][0] += 1
            if game_grid[y,x+1][0] != 'X':
                game_grid[y,x+1][0] += 1


def print_grid(size, minefield, show=False):
    """prints out the grid"""

    print("   " + "  ".join([chr(x + 65) for x in range(size)]))
    for i in range(size):
        print(chr(i + 65) + "  " + "  ".join([format_cell(minefield[i, x], show) for x in range(size)]))


def get_coord(c, size):
    """returns coordinates from user"""
    i = ord(c) - 97

    if i < 0 or i >= size:
        raise ValueError

    return i


def read_coords(size):
    """asks user to input coordinates in order to uncover a cell"""

    while True:
        l = input("Enter grid coordinates (y,x): ").strip().lower()

        coords_match = COORD_RE.match(l)
        if coords_match is not None:
            try:
                coords = (get_coord(l[0], size), get_coord(l[1], size))
                break
            except ValueError:
                print('Out of Range')
        else:
            print('Invalid Coordinate Format')

    return coords[1], coords[0]


def clear_cells(size, minefield, x, y, visited):
    """checks cell and recursively checks surrounding
    cells depending on cell value"""
    v = visited

    if minefield[y,x][0] != 'X' and minefield[y,x][0] > 0:
        if (x,y) not in v:
            v.add((x,y))
        minefield[y, x][1] = True

    if minefield[y,x][0] == 'X':
        return True, 0

    if minefield[y,x][0] == 0 and minefield[y,x][1] is False:
        minefield[y,x][1] = True
        for (i, j) in list_adjc(size, x, y):
            if (i,j) not in v:
                v.add((i,j))
            clear_cells(size, minefield, i, j, visited=v)

    return False, len(visited)


cells_to_clear = s1**2 - mines
minesweeper = minesweeper_grid(s1)
insert_mines(minesweeper, s1, mines)

dead = False
visited = set()
cleared = 0

# game runs until dead or uncovered all
while dead is False and cells_to_clear > cleared:
    print_grid(s1, minesweeper)
    (x,y) = read_coords(s1)
    (dead, cleared) = clear_cells(s1, minesweeper, x, y, visited)

# print grid at end of game with all cells uncovered
print_grid(s1, minesweeper, True)

# end message
if dead:
    print('Sorry, you hit a bomb! Try again')
else:
    print("Congratulations! You've uncovered all!")
