def areSimilar(a, b):
    aSort = sorted(a)
    bSort = sorted(b)
    compare = lambda a,b: len(a)==len(b) and len(a)<=sum([1 for i,j in zip(a,b) if i==j])
    almostCompare = lambda a,b: len(a)==len(b) and len(a)<=(sum([1 for i,j in zip(a,b) if i==j])+2)
    return compare(aSort, bSort) and almostCompare(a,b)
