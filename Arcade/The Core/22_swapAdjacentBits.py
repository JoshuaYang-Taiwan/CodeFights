def swapAdjacentBits(n):
    return int("".join(sum(([[a[1],a[0]] for a in ([(list(str(bin(n)[2:])) if len(list(str(bin(n)[2:])))%2==0 else ["0"]+list(str(bin(n)[2:])))[i:i+2] for i in range(0,len((list(str(bin(n)[2:])) if len(list(str(bin(n)[2:])))%2==0 else [0]+list(str(bin(n)[2:])))),2)])]),[])),2)
