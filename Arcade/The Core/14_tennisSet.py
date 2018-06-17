def tennisSet(score1, score2):
    score = [score1,score2]
    score.sort()
    if score[1] <= 7:
        if score[1] == 6 and score[0] < 5:
            return True
        elif score[1] == 7 and score[0] >= 5 and score[0] < 7:
            return True
        else:
            return False
            
    else:
        return False
