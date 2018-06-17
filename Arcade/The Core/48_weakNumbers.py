import math
def weakNumbers(n):
    divisorCounts = []
    for i in range(1,n+1):
        divisorCounts.append(countDivisor(i))
        
    weakness = []
    for i in range(len(divisorCounts)):
        count = 0
        for j in range(i):
            if divisorCounts[j] > divisorCounts[i]:
                count += 1
        weakness.append(count)
    return max(weakness),weakness.count(max(weakness))

def countDivisor(n):
    count = 1
    for i in range(1,n//2+1):
        if n % i == 0:
            count += 1
    return count
