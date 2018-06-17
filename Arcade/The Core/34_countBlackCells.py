import math
def countBlackCells(n, m):
    return n + m + math.gcd(n, m) -2
