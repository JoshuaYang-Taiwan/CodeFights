def isIPv4Address(inputString):
    myList = inputString.split(".")
    try:
        myList = [float(i) for i in myList]
    except:
        return False
    if len(myList) == 4:
        for i in myList:
            if i < 0 or i > 255:
                return False
        return True
    else:
        return False