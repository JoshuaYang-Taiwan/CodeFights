def sumUpNumbers(inputString):
    for e in inputString:
        if not e.isdigit():
            inputString = inputString.replace(e," ")
    return sum([int(e) for e in inputString.split()])
