def crosswordFormation(words):
    count = 0
    for w1 in range(4):
        word_1 = words[w1]
        for iw1 in range(len(word_1)-1):
            for w2 in range(4):
                if w1 == w2:
                    continue
                word_2 = words[w2]
                for iw2 in range(1, len(word_2)):
                    if word_2[iw2] != word_1[iw1]:
                        continue
                    for jw2 in range(iw2-1):
                        for w3 in range(4):
                            if w3 == w2 or w3 == w1:
                                continue
                            word_3 = words[w3]
                            word_4 = words[6-w1-w2-w3]
                            if iw2 - jw2 >= len(word_4):
                                continue
                            for iw3 in range(len(word_3)-1):
                                if word_3[iw3] != word_2[jw2]:
                                    continue
                                for jw3 in range(iw3+2, len(word_3)):
                                    jw1 = iw1 + (jw3-iw3)
                                    if jw1 >= len(word_1):
                                        continue
                                    for iw4 in range(len(word_4)):
                                        if word_4[iw4] != word_3[jw3]:
                                            continue
                                        jw4 = iw4 + (iw2-jw2)
                                        if jw4 >= len(word_4):
                                            break
                                        if word_1[jw1] != word_4[jw4]:
                                            continue
                                        count += 1
    return count