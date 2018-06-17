def electionsWinners(votes, k):
    count = 0
    maxNum = max(votes)
    for i in range(len(votes)):
        if votes[i] + k > maxNum:
            count += 1
    if k == 0 and votes.count(maxNum) == 1:
        count = 1
    return count
