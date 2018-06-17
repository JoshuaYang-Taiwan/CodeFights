def growingPlant(upSpeed, downSpeed, desiredHeight):
    count = 0
    while True:
        count += 1
        desiredHeight -= upSpeed
        if desiredHeight <= 0 : break
        desiredHeight += downSpeed
    return count
