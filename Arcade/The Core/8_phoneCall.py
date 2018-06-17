def phoneCall(min1, min2_10, min11, s):
    if s < min1:
        return 0
    if s is min1:
        return 1
    if s - min1 <= min2_10*9:
        return 1 + (s-min1) // min2_10
    return (s-min1-(min2_10*9)) // min11 + 10
