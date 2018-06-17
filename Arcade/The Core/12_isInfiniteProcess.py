def isInfiniteProcess(a, b):
    if a == b:
        return False
    if a > b:
        return True
    return isInfiniteProcess(a+1,b-1)
