##==============================================================
## Cuiyin Chen (20708813)
## CS 116 Winter 2018
##==============================================================
import math
import check

# Data definition 

# A MineGrid is a (listof (listof Bool))
# Requires:  All lists are non-empty
#            Each (listof Bool) has the same length 

# note: True means mine, False means safe

# A MineBoard is a (listof (listof Str))
# Requires: Each string is either a mine ('*') hidden(' ')
#             or safe (a digit between '0' and '8')
#           All lists are non-empty
#           Each (listof Str) has the same length



# Example board

grid3x3 = [[True ,False,False],
           [False,False,False],
           [False,False,True]]

board3x3 = [[' ', '1', '0'],
            [' ', '2', '1'],
            [' ', ' ', '*']]


grid1 = [[True ,False,False],[False,True,False],[True,False,True]]
grid2 = [[True ,True,True],[True,True,True],[True,True,True]]
grid3 = [[False ,False,False],[False,False,False],[False,False,False]]
grid4 = [[False ,True,False],[True,True,False],[True,False,False]]
grid5 = [[False, True], [True, True]]
grid6 = [[True, True, False, False], [False, False, False, True],\
         [True, False, True, False], [True, False, False, True]]


# reveal(grid,board, row, col) reveals the tile at the given row and col(umn)
#   in board, using the mine positions from grid
# reveal: MineGrid MineBoard -> None
# requires: grid and board have the same dimensions and are consistent
#           0 <= row < height of board
#           0 <= col < width  of board
# effects: board is mutated

def reveal(grid,board,row,col):
    if grid[row][col]:
        board[row][col] = '*'
    else:
        board[row][col] = str(count_mines(grid,row,col))
    return board[row][col]

## helper function for count_mines
## count_one(grid, rw, cl) returns 1 if there is a mine in the position
##   of the rwth row, clth column, where rw is the number representing the 
##   row number and cl is the number representing the column number; returns
##   0 if there is no mines in this position of the MineGrid grid
## count_one: MineGrid Nat Nat -> (anyof 1 0)

def count_one(grid, rw, cl):
    if rw >= len(grid) or cl >= len(grid[0]):
        return 0
    if grid[rw][cl] == True:
        return 1
    return 0


## count_mines(grid, row, col) returns how many mine tiles are adjacent
##   to the tile at the position of the rowth row, colth column in the
##   MineGrid grid
## count_mines: MineGrid Nat Nat -> Nat
## Require: the coners are only adjacent to 3 other tiles
## Examples:
##   count_mines(grid1, 0, 1) => 2
##   count_mines(grid3, 0, 0) => 0

def count_mines(grid,row,col):
    pos1 = count_one(grid, row-1, col-1)
    pos2 = count_one(grid, row-1, col)
    pos3 = count_one(grid, row-1, col+1)
    pos4 = count_one(grid, row, col-1)
    pos6 = count_one(grid, row, col+1)
    pos7 = count_one(grid, row+1, col-1)
    pos8 = count_one(grid, row+1, col)
    pos9 = count_one(grid, row+1, col+1)  
    if row >= len(grid) or col >= len(grid[0]):
        return 0
    if row-1 < 0 and col-1 < 0:
        return pos6+pos8+pos9
    if row-1 < 0 and col+1 > len(grid[0]):
        return pos4+pos7+pos8
    if col-1 < 0 and row+1 > len(grid):
        return pos2+pos3+pos6
    if row+1 >= len(grid) and col+1 >= len(grid[0]):
        return pos1+pos2+pos4
    if row-1 < 0:
        return pos4+pos6+pos7+pos8+pos9    
    if row+1 > len(grid):
        return pos1+pos2+pos3+pos4+pos6
    if col+1 > len(grid[0]):
        return pos1+pos2+pos4+pos7+pos8
    if col-1 < 0:
        return pos1+pos2+pos4+pos7+pos8
    return pos1+pos2+pos4+pos6+pos7+pos8+pos9

## Tests:
check.expect('t1', count_mines(grid2, 2, 2,), 3)
check.expect('t2', count_mines(grid2, 3, 1,), 0)
check.expect('t3', count_mines(grid3, 1, 1,), 0)
check.expect('t4', count_mines(grid4, 0, 0,), 3)
check.expect('t5', count_mines(grid1, 2, 1,), 3)
check.expect('t6', count_mines(grid2, 0, 2,), 3)
check.expect('t7', count_mines(grid3, 1, 0,), 0)
check.expect('t8', count_mines(grid4, 1, 2,), 2)
check.expect('t9', count_mines(grid1, 0, 1,), 2)
check.expect('t10', count_mines(grid2, 2, 0,), 3)
check.expect('t11', count_mines(grid5, 2, 2), 0)
check.expect('t12', count_mines(grid6, 3, 2), 2)
