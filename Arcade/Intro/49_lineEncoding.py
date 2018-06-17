def lineEncoding(s):
    i = 0
    nw = ""
    while i < len(s):
        ct = 1
        v = s[i]
        if i < len(s)-1 and s[i] == s[i + 1]:
            while i < len(s) -1 and s[i] == s[i+1]:
                ct += 1
                i += 1
            nw += str(ct) + v
        else:
            nw += v
        i += 1
    return nw