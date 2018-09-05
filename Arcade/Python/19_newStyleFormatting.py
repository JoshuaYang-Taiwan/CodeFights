def newStyleFormatting(s):
    s = s.replace('%%', '%_')
    print( s)
    s = re.sub(r'%[bcdeEfFgGnosxX]', r'{}', s)
    print(s)
    s = s.replace('%_', '%')
    print(s)
    return s
