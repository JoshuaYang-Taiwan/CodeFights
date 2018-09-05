def isCaseInsensitivePalindrome(inputString):
    inputString = inputString.lower()
    return inputString == inputString[::-1]
