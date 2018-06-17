def magicalWell(a, b, n):
    count = 0
    for i in range(n):
        count += a * b
        a += 1
        b += 1
    return count
    
