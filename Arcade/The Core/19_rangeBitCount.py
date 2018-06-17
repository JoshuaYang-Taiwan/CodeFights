def rangeBitCount(a, b):
    list = [int(i) for i in range(a,b+1)]
    count = 0
    for item in list:
        for num in bin(item)[2:]:
            count += int(num)
    return count
