def arrayMaxConsecutiveSum(inputArray, k):
    p=sum(a[0:k])
    maxi=p
    for i in range(k,len(a)):
        p = p + a[i]-a[i-k]
        if p>maxi:
            maxi=p
    return maxi
