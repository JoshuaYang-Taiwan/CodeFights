def differentSquares(matrix):
    squares=[]
    count = 0
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            square=[matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
            if square not in squares:
                squares.append(square)
                count += 1
    return count