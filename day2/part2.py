with open("input.txt") as f:
    sorted_lines = sorted(f)
    for a, b in zip(sorted_lines, sorted_lines[1:]):
        if len(a) != len(b):
            continue
        i_diff = -1
        for j, (c1, c2) in enumerate(zip(a, b)):
            if c1 != c2:
                if i_diff == -1:
                    i_diff = j
                else:
                    break
        else:
            print(a[:i_diff] + a[i_diff+1:])
            break
