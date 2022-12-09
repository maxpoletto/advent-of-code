def move(d, h, t, state):
    h = (h[0] + d[0], h[1] + d[1])
    if max(abs(t[0]-h[0]), abs(t[1]-h[1])) > 1:
        x = 1 if t[0] < h[0] else -1 if t[0] > h[0] else 0
        y = 1 if t[1] < h[1] else -1 if t[1] > h[1] else 0
        t = (t[0]+x, t[1]+y)
    if state:
        state.add(t)
    return h, t

def move_rope(d, r, state):
    r[0] = (r[0][0] + d[0], r[0][1] + d[1])
    for i in range(1, len(r)):
        r[i-1], r[i] = move((0, 0), r[i-1], r[i], None)
    state.add(r[9])

dirs = { "R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1) }
def part1():
    h, t = (0,0), (0,0)
    state = { t }
    with open("input/input09.txt") as f:
        for l in f:
            a, b = l.strip().split()
            dir, dist = dirs[a], int(b)
            for i in range(dist):
                h, t = move(dir, h, t, state)
    print(len(state))

def part2():
    rope = [ (0,0) for i in range(10) ]
    state = { rope[9] }
    with open("input/input09.txt") as f:
        for l in f:
            a, b = l.strip().split()
            dir, dist = dirs[a], int(b)
            for i in range(dist):
                move_rope(dir, rope, state)
    print(len(state))

part1()
part2()
