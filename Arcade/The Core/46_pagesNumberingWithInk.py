def pagesNumberingWithInk(current, numberOfDigits):
    while True:
        numberOfDigits -= len(str(current))
        if numberOfDigits < 0:
            return current -1
        current += 1
