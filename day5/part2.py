import string

def match(a, b):
    return a != b and a.lower() == b.lower()

def react(units, ignore=None):
    changed = True
    if ignore:
        units = [u for u in units if u not in ignore]
    while changed:
        changed = False
        result = []
        i = 0
        while i < len(units):
            cur = units[i]
            if i == len(units) - 1:
                result.append(cur)
                break
            next_one = units[i+1]
            if match(cur, next_one):
                changed = True
                i += 2
                continue
            else:
                result.append(cur)
                i += 1
        units = result
    return units

with open("input.txt") as f:
    units = f.read()
    units = list(units.strip())
    minimum = len(units)
    for l in string.lowercase:
        left = react(units, (l, l.upper()))
        if len(left) < minimum:
            minimum = len(left)
    print minimum
