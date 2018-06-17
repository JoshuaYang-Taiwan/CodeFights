def digitsProduct(product):
    if product == 0:
        return 10
    for i in range(2*3*4*5*6*7*8*9):
        r = 1
        for j in str(i):
            r *= int(j)
        if r == product:
            return i
    return -1