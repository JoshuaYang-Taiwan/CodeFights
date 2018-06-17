def digitDegree(n):
    count = 0
    while(len(str(n)) != 1):
        n = sum(map(int, str(n)))
        count += 1
    return count

        
