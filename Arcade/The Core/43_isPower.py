def isPower(n):
    divisors = []
    while n != 1:  
        for i in range(1, n + 1):  
            if (n % i) == 0 and i != 1:  
                n = int(n / i)  
                divisors.append(i)
                break
    if len(list(set(divisors))) == 1 and len(divisors) != 1:
        return True
    for i in divisors:
        if divisors.count(i)%2 != 0:
            return False
    return True
    
            
