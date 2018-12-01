with open("input.txt") as f:
    print(sum(int(l.strip()) for l in f))
