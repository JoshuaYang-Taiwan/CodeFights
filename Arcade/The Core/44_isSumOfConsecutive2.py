def isSumOfConsecutive2(n):
    result = 0
    for j in range(1,n):
        total = 0
        for i in range(j,n):
            total += i
            if total == n:
                result += 1
            if total > n:
                break
    return result