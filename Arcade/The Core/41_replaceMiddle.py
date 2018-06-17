def replaceMiddle(arr):
    return arr if len(arr)%2 != 0 else arr[0:len(arr)//2-1] + [arr[len(arr)//2-1]+arr[len(arr)//2]] + arr[len(arr)//2+1:]
