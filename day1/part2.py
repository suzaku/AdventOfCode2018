import itertools

with open("input.txt") as f:
    changes = (int(l.strip()) for l in f)
    freq = 0
    seen = {freq}
    for c in itertools.cycle(changes):
        freq += c
        if freq in seen:
            print(freq)
            break
        else:
            seen.add(freq)
