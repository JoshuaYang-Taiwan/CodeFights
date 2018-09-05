def check9(group):
    v = [c for c in group if c != '.']
    return len(v) == len(set(v))

def sub(g, i, j):
    for y in range(3*j, 3*j+3):
        for x in range(3*i, 3*i+3):
            yield g[y][x]

def sudoku2(grid):
    for l in grid:
        if not check9(l):
            return False
    for i in range(9):
        l = [v[i] for v in grid]
        if not check9(l):
            return False
    for i in range(3):
        for j in range(3):
            l = list(sub(grid, i, j))
            if not check9(l):
                return False
    return True

