def validTime(time):
    return len(time)<=5 and 0<=int(time.split(":")[0])<=23 and 0<=int(time.split(":")[1])<=59
