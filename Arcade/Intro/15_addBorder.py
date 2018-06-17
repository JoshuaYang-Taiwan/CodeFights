def addBorder(picture):
    width = len(picture[0]) + 2
    height = len(picture) + 2
    myList = []
    for row in range(height):
        line = ""
        if row == 0 or row == height-1:
            line = "".join("*" for i in range(width))
        else:
            line = "*" + picture[row-1] + "*"
        myList.append(line)
    return myList
            
            
