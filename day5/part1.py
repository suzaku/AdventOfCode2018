def match(a, b):
    return a != b and a.lower() == b.lower()

def react(units):
    changed = True
    while changed:
        changed = False
        result = []
        i = 0
        while i < len(units):
            if i == len(units) - 1:
                result.append(cur)
                break
            cur = units[i]
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
    units = react(units)
    print len(units)
