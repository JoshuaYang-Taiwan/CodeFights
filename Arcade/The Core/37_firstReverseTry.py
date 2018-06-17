def firstReverseTry(arr):
    return arr[-1:] + arr[1:-1] + arr[:1] if len(arr) > 1 else arr
