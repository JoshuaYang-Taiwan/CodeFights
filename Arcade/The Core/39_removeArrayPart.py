def removeArrayPart(inputArray, l, r):
    return [item for index,item in enumerate(inputArray) if not l<=index<=r]
