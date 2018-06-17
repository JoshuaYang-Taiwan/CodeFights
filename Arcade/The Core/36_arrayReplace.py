def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [item if item != elemToReplace else substitutionElem for item in inputArray ]
