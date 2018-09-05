def isCryptSolution(crypt, solution):
    d = dict(solution)
    a = "".join([d[w] for w in crypt[0]])
    b = "".join([d[w] for w in crypt[1]])
    c = "".join([d[w] for w in crypt[2]])
    notLeadingZero = lambda numStr : False if len(numStr) > 1 and numStr[0] is "0" else True
    return notLeadingZero(a) and notLeadingZero(b) and notLeadingZero(c) and int(a)+int(b)==int(c)
