def sortByHeight(a):
    myList = list(a)
    for i in range(a.count(-1)):
        myList.remove(-1)
    myList.sort()
    for index,item in enumerate(a):
        if item == -1:
            myList.insert(index,-1)
    return myList
        
