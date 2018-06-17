def squareDigitsSequence(a0):
    elements = [a0]
    num = a0
    while True:
        num = sumOfSquare(num)
        elements.append(num)
        if num in elements[:-1]:
            break
    return len(elements)

def sumOfSquare(n):
    result = 0
    listN = list(str(n))
    for i in listN:
        result += int(i)**2
    return result
    
