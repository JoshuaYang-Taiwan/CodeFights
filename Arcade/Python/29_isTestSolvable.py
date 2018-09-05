def isTestSolvable(ids, k):
    digitSum = lambda x : sum([int(e) for e in str(x)])

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
