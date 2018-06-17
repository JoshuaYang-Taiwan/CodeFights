def chessKnight(cell):
    x,y = ord(cell[0])-96, int(cell[1])
    a = x+2<9 and y+1<9
    b = x+1<9 and y+2<9
    c = x-1>0 and y+2<9
    d = x-2>0 and y+1<9
    e = x-2>0 and y-1>0
    f = x-1>0 and y-2>0
    g = x+1<9 and y-2>0
    h = x+2<9 and y-1>0
    return a+b+c+d+e+f+g+h
    
