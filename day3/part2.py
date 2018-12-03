def parse_rec(l):
    id_, info = l.split('@', 1)
    info = info.strip()
    pos_part, size_part = info.split(':', 1)
    x, y = [int(i) for i in pos_part.split(',', 1)]
    width, height = [int(i) for i in size_part.strip().split('x', 1)]
    return id_, ((x, y), width, height)


with open("input.txt") as f:
    space = []
    for i in range(1000):
        space.append([0] * 1000)

    recs = [parse_rec(l) for l in f]
    for id_, ((x, y), width, height) in recs:
        for row in space[y:y+height]:
            for j in range(x, x+width):
                row[j] += 1
    for id_, ((x, y), width, height) in recs:
        if all(row[j] == 1 for j in range(x, x+width) for row in space[y:y+height]):
            print(id_)
            break
