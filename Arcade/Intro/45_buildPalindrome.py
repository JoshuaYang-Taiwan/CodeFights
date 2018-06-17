def buildPalindrome(str):
    cut_str=str
    while True:
        if cut_str[::-1]==cut_str: break
        cut_str = cut_str[1::]
    remaining = str[:len(str)-len(cut_str):]
    c=0
    while True:
        if str[::-1]==str: return str
        str += remaining[::-1][c]
        c += 1
        