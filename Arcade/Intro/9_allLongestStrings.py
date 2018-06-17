def allLongestStrings(inputArray):
    long = 0
    result = []
    for item in inputArray:
        long = len(item) if len(item) > long else long
    for item in inputArray:
        if len(item) is long:
            result.append(item)
    return result
