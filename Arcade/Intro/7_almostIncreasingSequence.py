def almostIncreasingSequence(sequence):
    if sequence[0] >= sequence[1]:
        myList = list(sequence[1:])
        return increasingSequence(myList)
    else:
        now = sequence[0]
        count = 0
        for i in range(1,len(sequence)):
            if sequence[i] > now:
                now = sequence[i]
            else:
                count += 1
        return count <= 1
    
def increasingSequence(sequence):
    if sequence == 1:
        return True
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return False
    return True