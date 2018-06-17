def isBeautifulString(inputString):
    myList = []
    for i in range(97,123):
        myList.append(inputString.count(chr(i)))
    for i in range(25):
        if myList[i] < myList[i+1]:
            return False
    return True
