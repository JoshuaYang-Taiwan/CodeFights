def appleBoxes(k):
    count = 0
    for i in range(1,k+1):
        if i % 2 != 0:
            count -= i**2
        else:
            count += i**2
    return count
