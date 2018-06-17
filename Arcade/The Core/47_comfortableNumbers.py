def comfortableNumbers(l, r):
    count = 0
    for i in range(l,r+1):
        for j in range(i+1,r+1):
            if comfortableWithEach(i,j):
                count += 1
    return count
def comfortableWithEach(a,b):
    if a >= b-sumOfDigits(b) and a <= b+sumOfDigits(b) and b >= a-sumOfDigits(a) and b <= a+sumOfDigits(a):
        return True
    else:
        return False
def sumOfDigits(x):
    return sum([int(i) for i in list(str(x))])

    
    