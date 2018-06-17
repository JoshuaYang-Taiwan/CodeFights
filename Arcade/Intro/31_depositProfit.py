def depositProfit(deposit, rate, threshold):
    count = 1
    while True:
        deposit = deposit * (100 + rate)/100
        if deposit >= threshold:
            return count
        else:
            count += 1
