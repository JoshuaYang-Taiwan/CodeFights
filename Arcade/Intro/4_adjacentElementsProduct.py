def adjacentElementsProduct(inputArray):
    result = inputArray[0] * inputArray[1]
    for i in range(len(inputArray)-1):
        num = inputArray[i] * inputArray[i+1]
        result = num if num > result else result
    return result
