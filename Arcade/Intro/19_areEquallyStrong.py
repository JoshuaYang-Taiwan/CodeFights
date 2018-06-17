def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    yl = yourLeft
    yr = yourRight
    fl = friendsLeft
    fr = friendsRight
    return True if yl+yr == fl+fr and (yl == fl or yl == fr) else False
