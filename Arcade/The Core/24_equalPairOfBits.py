def equalPairOfBits(n, m):
    return 2**(bin(n^m)[:1:-1].count('1') if bin(n^m)[:1:-1].find('0') == -1 else bin(n^m)[:1:-1].find('0'))
