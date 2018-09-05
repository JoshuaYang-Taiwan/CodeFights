def wordPower(word):
    num = {string.ascii_lowercase[i-1] : i for i in range(27)}
    return sum([num[ch] for ch in word])
