import collections

def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]


def uniqueCombinations(size, elements):
    if len(elements) == 1:
        return []
    firstElement = elements[0]
    theRest = elements[1:]
    spread = theRest if size == 2 else uniqueCombinations(size - 1, theRest)
    combos = list(map(lambda x: flatten([firstElement] + [x]), spread)) + uniqueCombinations(size, theRest)
    return combos
