import numpy as np
def sudoku(grid):
    grid = np.array(grid)
    for row in range(9):
        if not checkRepeat(grid[row]):
            return False
    for col in range(9):
        if not checkRepeat(grid[:,col]): 
            return False
    for row in range(0,9,3):
        for col in range(0,9,3):
            if not checkRepeat(grid[row:row+3,col:col+3]):
                return False
                
    return True
    
    
def checkRepeat(list):
    array = np.array(list)
    array = array.reshape(-1)
    array2 = np.unique(array)
    if len(array) == len(array2):
        return True
    else:
        return False