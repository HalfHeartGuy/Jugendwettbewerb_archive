
import sudoku_3
from sudoku_3 import *
import random
from random import *



# define a  function to return a suduku matrix
def suduku_matrix():
    return zerosInSudoku("leicht", sudokuGenerator())
