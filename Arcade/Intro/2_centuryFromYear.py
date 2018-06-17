def centuryFromYear(year):
    if year%100 is not 0:
        return year // 100 + 1
    else:
        return year // 100
