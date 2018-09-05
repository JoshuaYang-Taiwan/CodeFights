def messageFromBinaryCode(code):
    codeList = [code[i:i+8] for i in range(0, len(code), 8)]
    codeList = [int(e,2) for e in codeList]
    codeList = [chr(e) for e in codeList]
    return "".join(codeList)