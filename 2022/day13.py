import functools

def parse():
    data = []
    with open('input/input13.txt') as f:
        for l in f:
            l = l.strip()
            if len(l) > 0:
                data.append(eval(l))
    return data

def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return -1
        if l > r:
            return 1
        return 0
    if isinstance(l, list) and isinstance(r, list):
        i = 0
        while i < len(l) and i < len(r):
            c = compare(l[i], r[i])
            if c != 0:
                return c
            i += 1
        if len(l) < len(r):
            return -1
        if len(l) > len(r):
            return 1
        return 0
    if isinstance(l, int):
        l = [l]
    elif isinstance(r, int):
        r = [r]
    return compare(l, r)

def part1():
    data = parse()
    i, j, t = 1, 1, 0
    while j < len(data):
        if compare(data[j-1], data[j]) < 0:
            t += i
        i, j = i+1, j+2
    print(t)

def part2():
    data = parse()
    data.append([[2]])
    data.append([[6]])
    data.sort(key=functools.cmp_to_key(compare))
    r = 1
    for i in range(len(data)):
        if data[i] == [[2]] or data[i] == [[6]]:
            r *= (i+1)
    print(r)

part1()
part2()
