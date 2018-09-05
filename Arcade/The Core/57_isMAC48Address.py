def isMAC48Address(inputString):
    mylist = inputString.split("-")
    if not len(mylist) == 6:
        return False
    correctList = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    for e in mylist:
        if not len(e) == 2:
            return False
        if e[0] not in correctList or e[1] not in correctList:
            return False
    return True