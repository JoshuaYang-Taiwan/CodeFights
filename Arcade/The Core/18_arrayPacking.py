def fill_to_eight(a):
    while len(a)  != 8:
        a = "0" + a
    return a

def arrayPacking(a):
    a = a[::-1]
    res = []
    for e in a:
        if e == 0:
            res.append("00000000")
        else:
            z = fill_to_eight((bin(e)[2:]))
            print(z)
            res.append(z)
    return (int("".join(res),2))