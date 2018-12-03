def parse_rec(l):
    info = l.split('@', 1)[1].strip()
    pos_part, size_part = info.split(':', 1)
    x, y = [int(i) for i in pos_part.split(',', 1)]
    width, height = [int(i) for i in size_part.strip().split('x', 1)]
    return ((x, y), width, height)


with open("input.txt") as f:
    space = []
    for i in range(1000):
        space.append([0] * 1000)

    n = 0
    for l in f:
        (x, y), width, height = parse_rec(l)
        for row in space[y:y+height]:
            for j in range(x, x+width):
                if row[j] == 1:
                    n += 1
                row[j] += 1
    print(n)
