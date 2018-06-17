def additionWithoutCarrying(param1, param2):
    list1 = str(param1)
    list2 = str(param2)
    if len(list1) > len(list2):
        list2 = list2.zfill(len(list1))
    if len(list1) < len(list2):
        list1 = list1.zfill(len(list2))
    result = [str((int(a)+int(b))%10) for a,b in zip(list1,list2)]
    return int("".join(result))
