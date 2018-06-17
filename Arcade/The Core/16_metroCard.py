def metroCard(lastNumberOfDays):
    if lastNumberOfDays == 30:
        return [31]
    elif lastNumberOfDays == 31:
        return [28,30,31]
    elif lastNumberOfDays == 28:
        return [31]