from collections import defaultdict, Counter


def parse_minite(time_part):
    return int(time_part.split(':', 1)[1])


with open("input.txt") as f:
    lines = sorted(l.rstrip() for l in f)
    guard = None
    prev_min = None
    guard_sleeps = defaultdict(list)
    for l in lines:
        time_part, msg_part = l.split(']', 1)
        msg_part = msg_part.lstrip()
        if msg_part.startswith('Guard'):
            guard = msg_part[len('Guard') + 1:].split(' ', 1)[0]
            guard = int(guard[1:])
        else:
            minute = parse_minite(time_part)
            if msg_part.startswith('fa'):
                prev_min = minute
            elif msg_part.startswith("wa"):
                guard_sleeps[guard].append((prev_min, minute))

    max = None
    for guard, sleeps in guard_sleeps.items():
        total = 0
        counter = Counter()
        for start, end in sleeps:
            total += (end - start)
            for i in range(start, end):
                counter[i] += 1
        if max is None or total > max[0]:
            max = (total, guard, counter.most_common(1)[0][0])
    print max[1] * max[2]
