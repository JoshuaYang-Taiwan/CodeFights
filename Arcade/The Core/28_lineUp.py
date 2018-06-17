def lineUp(commands):
    count = 0
    isSameDirection = True
    
    for index,item in enumerate(commands):
        if item == "A" and isSameDirection:
            count +=1
        elif item == "A" and not isSameDirection:
             pass
        elif (item == "L" or item == "R") and not isSameDirection:
            count += 1
            isSameDirection = True
        elif (item == "L" or item == "R") and isSameDirection:
                isSameDirection = False
    return count
