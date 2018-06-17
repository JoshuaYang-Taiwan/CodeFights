def isSmooth(arr):
    return True if arr[0] == arr[-1] and arr[0] == (arr[len(arr)//2] if len(arr)%2!=0 else arr[len(arr)//2]+arr[len(arr)//2-1]) else False
