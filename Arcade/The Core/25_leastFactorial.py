def leastFactorial(n):
    fac = 1
    count = 1
    while True:
        fac *= count
        if fac >= n:
            return fac
        else:
            count += 1