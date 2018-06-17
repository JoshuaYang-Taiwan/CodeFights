def deleteDigit(n):
    deletedList = []
    nList = list(str(n))
    for e in nList:
        newList = list(nList)
        newList.remove(e)
        deletedList.append(int("".join(newList)))
    return max(deletedList)