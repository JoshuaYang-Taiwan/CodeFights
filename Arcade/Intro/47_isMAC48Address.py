def isMAC48Address(inputString):
    if len(inputString) != 17:
        return False
    myList = [item for items in inputString.split("-") for item in items]
    if len(myList) != 12:
        return False
    check = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    for e in myList:
        if check.count(e) == 0:
            return False
    return True
