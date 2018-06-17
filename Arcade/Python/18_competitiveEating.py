def competitiveEating(t, width, precision):
    return str("%.{}f".format(precision) % t).center(width)
