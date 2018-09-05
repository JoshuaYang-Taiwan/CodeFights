def firstNotRepeatingCharacter(s):
    d = {}
    for i,e in enumerate(s):
        if e in d.keys():
            d[e] = -1
        else:
            d[e] = i
    print(d)
    for e in s:
        if d[e] is not -1:
            return e
    return "_"
    