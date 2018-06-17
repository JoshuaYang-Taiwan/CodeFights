def arrayMaximalAdjacentDifference(inputArray):
    max = abs(inputArray[0] - inputArray[1])
    for i in range(len(inputArray)-1):
        n = abs(inputArray[i] - inputArray[i+1])
        max = n if n > max else max
    return max

