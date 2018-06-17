def mirrorBits(a):
    mylist = list(bin(a)[2:])
    mylist = mylist[::-1]
    mylist = "".join(mylist)
    return int(mylist,2)
