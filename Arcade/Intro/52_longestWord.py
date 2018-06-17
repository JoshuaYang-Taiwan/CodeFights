def longestWord(text):
    for e in text:
        if not e.isalpha():
            text = text.replace(e,"\t")
    textList = text.split("\t")
    lenList = [len(e) for e in textList]
    i = lenList.index(max(lenList))
    return textList[i]
