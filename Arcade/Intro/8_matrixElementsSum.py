def matrixElementsSum(matrix):
    for indexRow,row in enumerate(matrix):
        for indexCol,item in enumerate(row):
            if item is 0:
                for i in range(indexRow,len(matrix)):
                    matrix[i][indexCol] = 0
    sum = 0
    for i in matrix:
        for j in i:
            sum += j
    return sum
