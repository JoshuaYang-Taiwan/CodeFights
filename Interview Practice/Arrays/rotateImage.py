def rotateImage(a):
    list_of_tuples = zip(*a[::-1])
    return list(list_of_tuples)