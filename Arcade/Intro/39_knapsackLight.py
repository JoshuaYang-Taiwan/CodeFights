def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1+weight2 <= maxW:
        return value1+value2
    elif weight1 > maxW and weight2 > maxW:
        return 0
    elif weight1 > maxW and weight2 <= maxW:
        return value2
    elif weight1 <= maxW and weight2 > maxW:
        return value1
    elif value1 >= value2:
        return value1
    elif value1 <= value2:
        return value2
