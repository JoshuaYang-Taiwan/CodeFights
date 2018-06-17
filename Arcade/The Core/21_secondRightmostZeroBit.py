def secondRightmostZeroBit(n):
    return 2**(len(bin(n)[2:]) - (int(str(bin(n)[2:][::-1]).replace('0','1',1)[::-1].rfind('0'))+1))
