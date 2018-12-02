from collections import Counter

with open("input.txt") as f:
    n_twos = 0
    n_threes = 0
    for l in f:
        c = Counter(l)
        if any(n == 2 for n in c.values()):
            n_twos += 1
        if any(n == 3 for n in c.values()):
            n_threes += 1
    print(n_twos * n_threes)
