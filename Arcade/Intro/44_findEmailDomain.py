def findEmailDomain(address):
    index = address[::-1].find("@")
    return address[-index:]
