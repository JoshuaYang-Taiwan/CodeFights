def boxBlur(image):
    width = len(image[0])
    height = len(image)
    result = []
    for row in range(1,height-1):
        line = []
        for col in range(1,width-1):
            mylist = [i[col-1:col+2] for i in image[row-1:row+2]]
            line.append(int(sum(sum(i) for i in mylist)/9))
        result.append(line)
    return result