from pprint import pprint

def read_input():
    m = []
    with open("input/i06.txt") as f:
        for l in f:
            m.append(list(l.strip()))
    pos, cur = None, None
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] in '<>^v':
                pos = (r, c)
                cur = m[r][c]
                m[r][c] = '.'
                break
        if pos:
            break
    assert pos is not None
    return m, len(m), len(m[0]), pos, cur

dir = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

turn = {
    '^': '>',
    'v': '<',
    '<': '^',
    '>': 'v'
}

def part1():
    m, h, w, pos, cur = read_input()
    v = set()
    while (True):
        v.add(pos)
        d = dir[cur]
        p2 = (pos[0] + d[0], pos[1] + d[1])
        if p2[0] < 0 or p2[0] >= h or p2[1] < 0 or p2[1] >= w:
            break
        if m[p2[0]][p2[1]] != '.':
            cur = turn[cur]
            continue
        pos = p2
    print(len(v))

def part2():
    m, h, w, pos, cur = read_input()
    v = set()
    turns_r, turns_c, nturns = {}, {}, 0
    obs = set()
    while (True):
        v.add(pos)
        d = dir[cur]
        p2 = (pos[0] + d[0], pos[1] + d[1])
        if p2[0] < 0 or p2[0] >= h or p2[1] < 0 or p2[1] >= w:
            break
        if m[p2[0]][p2[1]] != '.':
            turns_r.setdefault(pos[0], []).append(pos[1])
            turns_c.setdefault(pos[1], []).append(pos[0])
            turns_r[pos[0]].sort()
            turns_c[pos[1]].sort()
            print('Turn at', pos, cur)
            cur = turn[cur]
            nturns += 1
            continue
        pos = p2
        if cur == '^':
            if (pos[0] in turns_r and
                pos[1] < turns_r[pos[0]][-1] and
                pos[0] > 0 and
                m[pos[0] - 1][pos[1]] == '.'):
                    obs.add((pos[0] - 1, pos[1]))
        elif cur == 'v':
            if (pos[0] in turns_r and
                pos[1] > turns_r[pos[0]][0] and
                pos[0] < h - 1 and
                m[pos[0] + 1][pos[1]] == '.'):
                    obs.add((pos[0] + 1, pos[1]))
        elif cur == '<':
            if (pos[1] in turns_c and
                pos[0] > turns_c[pos[1]][0] and
                pos[1] > 0 and
                m[pos[0]][pos[1] - 1] == '.'):
                    obs.add((pos[0], pos[1] - 1))
        elif cur == '>':
            if (pos[1] in turns_c and
                pos[0] < turns_c[pos[1]][-1] and
                pos[1] < w - 1 and
                m[pos[0]][pos[1] + 1] == '.'):
                    obs.add((pos[0], pos[1] + 1))
    print(len(obs))

part1()
part2()
