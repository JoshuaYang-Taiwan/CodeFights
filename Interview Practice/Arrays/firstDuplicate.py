def firstDuplicate(a):
    maxCount = 1
    for item in a:
        if a.count(item) > maxCount:
            maxCount = a.count(item)
    if maxCount == 1:
        return -1
    maxCountValues = []
    for item in a:
        if a.count(item) == maxCount:
            if item in maxCountValues:
                return item
            maxCountValues.append(item)
