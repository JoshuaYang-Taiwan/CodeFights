def avoidObstacles(inputArray):
    inputArray.sort()
    step = 1
    location = 0
    while True:
        if location not in inputArray:
            if location < max(inputArray):
                location += step
            else:
                return step
        else:
            step += 1
            location = 0