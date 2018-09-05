def isTandemRepeat(inputString):
    return inputString[0:len(inputString)//2] == inputString[len(inputString)//2:]
