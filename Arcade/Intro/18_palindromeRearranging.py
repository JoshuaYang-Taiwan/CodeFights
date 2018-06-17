def palindromeRearranging(inputString):
    latterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    countList = []
    for item in latterList:
        countList.append(inputString.count(item))
    falseCount = 0
    for item in countList:
        if not(item % 2 == 0):
            falseCount += 1;
    return falseCount <= 1
    
