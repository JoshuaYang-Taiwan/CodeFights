def shapeArea(n):
    if n == 1:
        return 1
    else:
        return (n-1)*4 + shapeArea(n-1)
