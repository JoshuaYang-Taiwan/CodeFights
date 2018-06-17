def isLucky(n):
    n = list(str(n))
    n = [int(i) for i in n]
    s1 = n[0:len(n)//2]
    s2 = n[len(n)//2:]
    score1 = 0
    score2 = 0
    for e in s1:
        score1 += int(e)
    for i in s2:
        score2 += int(i)
    return score1 == score2
    
