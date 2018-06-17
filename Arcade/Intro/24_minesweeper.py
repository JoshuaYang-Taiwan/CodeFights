def minesweeper(matrix):
    width = len(matrix[0])+2
    height = len(matrix)+2
    newMatrix = []
    for row in range(height):
        line = []
        for col in range(width):
            if row == 0 or row == height-1 or col == 0 or col == width -1:
                line.append(False)
            else:
                line.append(matrix[row-1][col-1])
        newMatrix.append(line)
    result = []
    for row in range(height):
        if row == 0 or row == height-1:continue
        line = []
        for col in range(width):
            if col == 0 or col == width -1:continue
            else:
                neighbor = [i[col-1:col+2] for i in newMatrix[row-1:row+2]]
                neighbor = sum(neighbor,[])
                trueCount = neighbor.count(True)
                if matrix[row-1][col-1] == True:
                    line.append(trueCount-1)
                else:
                    line.append(trueCount)
        result.append(line)
    return result
