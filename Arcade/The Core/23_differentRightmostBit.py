def differentRightmostBit(n, m):
    return 2 ** [index for index,item in enumerate(bin(n^m)[:1:-1]) if item == "1"][0]
