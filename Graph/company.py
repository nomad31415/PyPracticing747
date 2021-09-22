def items_in_compartments(string, startInd, endInd):
    strings = map(lambda t: string[t[0]:t[1] + 1], zip(startInd, endInd))
    return list(map(lambda s: s.strip('*').count('*'), strings))
