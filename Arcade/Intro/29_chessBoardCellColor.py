def alphabeticShift(inputString):
    return "".join([("a" if ord(i) == 122 else chr(ord(i)+1))for i in list(inputString)])
