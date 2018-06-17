def increaseNumberRoundness(n):
    isZero = True
    for i in str(n)[::-1]:
        if i != "0" and isZero:
            isZero = False
        elif i == "0" and not isZero:
            return True
    return False
        
        
