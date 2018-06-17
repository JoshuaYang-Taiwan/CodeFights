def rounders(value):
    valueS = str(value)
    if len(valueS) == 1:
        return value
    last = int(valueS[-1])
    if last <= 4:
        return 10 * rounders(value // 10)
    else:
        return 10 * rounders(value // 10 + 1)