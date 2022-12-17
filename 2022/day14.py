import functools

# returns a wall map and the relative x-coordinate of the sand source (logically at 500,0)
def parse(part):
    walls = []
    ul, br = [10000, 0], [0, 0]
    with open('input/input14.txt') as f:
        for l in f:
            ps = l.strip().split(' -> ')
            pt = []
            for p in ps:
                xs, ys = p.split(',')
                x, y = int(xs), int(ys)
                ul = [min(ul[0], x), min(ul[1], y)]
                br = [max(br[0], x), max(br[1], y)]
                pt.append((x, y))
            walls.append(pt)
    if part == 2: # build a wide floor
        ul[0] = 0
        br = [br[0] * 2, br[1] + 2]
        walls.append([[0, br[1]], br])
    # build map
    w = br[0] - ul[0] + 3 # +2 for padding
    h = br[1] - ul[1] + 2 # +1 for padding
    m = [['.' for _ in range(w)] for _ in range(h)]
    # draw walls
    for wall in walls:
        for i in range(len(wall) - 1):
            x1, y1 = wall[i]
            x2, y2 = wall[i + 1]
            dx = 1 if x2 >= x1 else -1
            dy = 1 if y2 >= y1 else -1
            for x in range(x1, x2+dx, dx):
                for y in range(y1, y2+dy, dy):
                    m[y - ul[1]][x - ul[0] + 1] = '#'
    # compute source x-coordinate
    sx = 500 - ul[0] + 1 # source x-coordinate
    m[0][sx] = '+'
    return m, sx

def drop(m, s):
    p = [s, 0]
    while p[1] < len(m)-1:
        if m[p[1]+1][p[0]] == '.':
            p[1] += 1
            continue
        if p[0] > 0 and m[p[1]+1][p[0]-1] == '.':
            p[0] -= 1
            p[1] += 1
            continue
        if p[0] < len(m[0])-1 and m[p[1]+1][p[0]+1] == '.':
            p[0] += 1
            p[1] += 1
            continue
        m[p[1]][p[0]] = 'o'
        break
    return p

def part1():
    m, s = parse(1)
    n = 0
    while True:
        p = drop(m, s)
        if p[1] == len(m)-1:
            break
        n += 1
    print(n)

def part2():
    m, s = parse(2)
    n = 0
    while True:
        p = drop(m, s)
        n += 1
        if p[1] == 0:
            break
    print(n)

part1()
part2()
