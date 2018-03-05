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


grid1 = [[True ,False,False],
         [False,True,False],
         [True,False,True]]

grid2 = [[True ,True,True],
         [True,True,True],
         [True,True,True]]

grid3 = [[False ,False,False],
         [False,False,False],
         [False,False,False]]

grid4 = [[False ,True,False],
         [True,True,False],
         [True,False,False]]

board1 = [[' ', '2', '1'],
          [' ', '*', ' '],
          [' ', '3', ' ']]

board2 = [[' ', ' ', ' '],
          [' ', '*', ' '],
          [' ', ' ', ' ']]

board3 = [['0', '0', '0'],
          ['0', '0', '0'],
          ['0', '0', '0']]

board4 = [['3', ' ', '2'],
          [' ', ' ', '2'],
          [' ', '3', '1']]


# game_lost(board) returns true if board contains one or more revealed mines,
#   false otherwise
# game_lost: GameBoard -> Bool

def game_lost(board):
    mined_rows = len(list(filter(lambda row: '*' in row, board)))
    return mined_rows != 0


## game_won(grid, board) returns True if the game (represented by the MineGrid
##   grid and the MineBoard board) has been won; and returns False otherwise
## game_won: MineGrid MineBoard -> Bool
## Examples:
##   game_won(grid1, board1) => False
##   game_won(grid4, board4) => True

def game_won(grid,board):
    count_mines = len(list(filter(lambda row: True in row, grid)))
    count_reveal = len(list(filter(lambda row: ' ' in row, board)))
    if game_lost(board):
        return False
    if count_mines == count_reveal:
        return True
    return False #eagle told me I forgot the return

## Tests:
check.expect('t1', game_won(grid1, board1), False)
check.expect('t2', game_won(grid2, board2), False)
check.expect('t3', game_won(grid3, board3), True)
check.expect('t4', game_won(grid4, board4), True)
