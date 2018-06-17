def extractEachKth(inputArray, k):
    return [item for index,item in enumerate(inputArray) if index % k != k-1]
