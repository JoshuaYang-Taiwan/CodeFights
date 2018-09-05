def fileNaming(names):
    result = []
    for name in names:
        if name in result:
            result.append(addSuffix(name,result))
        else:
            result.append(name)
    return result
            
    
def addSuffix(name,result):
    count = 1
    newName = name + "(" + str(count) + ")"
    while newName in result:
        count += 1
        newName = name + "(" + str(count) + ")"
    return newName