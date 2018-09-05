import numpy as np

def spiralNumbers(n):
    array = np.full((n,n),None)
    for times in range((n//2 if n//2 == 0 else n//2+1)):
        if n-times*2 == 0:
            break
        array[times:n-times,times:n-times] = makeFrame(n-times*2,count(n,times))     
    return array

def count(n,times):
    if times == 0:
        return 1
    else:
        return (n-(times-1)*2-1)*4 + count(n,times-1)
    
def makeFrame(side,n):
    if side == 1:
        return [[n]]
    else:
        array = np.full((side,side),None)
        frameSide = side-1
        array[0][0:frameSide] = np.arange(n,n+frameSide)
        array = np.rot90(array)
        array[0][0:frameSide] = np.arange(n+frameSide,n+frameSide+frameSide)
        array = np.rot90(array)
        array[0][0:frameSide] = np.arange(n+frameSide*2,n+frameSide+frameSide*2)  
        array = np.rot90(array)
        array[0][0:frameSide] = np.arange(n+frameSide*3,n+frameSide+frameSide*3)  
        array = np.rot90(array)
        return array.tolist()
    