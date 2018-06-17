def commonCharacterCount(s1, s2):
    counts = 0
    counts1=0
    counts2=0
    letters= set.intersection(set(s1), set(s2))
    for letter in letters:
        counts1 += s1.count(letter)
        counts2 += s2.count(letter)
        counts += min(counts1, counts2)
        counts1 = 0
        counts2 = 0
    return counts
