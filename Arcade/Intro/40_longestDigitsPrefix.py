def longestDigitsPrefix(inputString):
    result = ""
    for e in inputString:
        if e.isdigit():
            result += e
        else:
            break
    return result
