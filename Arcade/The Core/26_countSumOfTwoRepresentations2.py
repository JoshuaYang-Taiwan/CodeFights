def countSumOfTwoRepresentations2(n, l, r):
    count = 0
    for a in range(l,r+1):
        if l <= a <= n-a <= r:
            count += 1
    return count
        
