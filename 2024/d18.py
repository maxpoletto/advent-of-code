from collections import deque

def read_input():
    sz = 71
    m = [ ['#'] * (sz + 2) ]
    m +=  [ ['#'] + ['.'] * sz + ['#'] for _ in range(sz) ]
    m +=  [ ['#'] * (sz + 2)]
    n = []
    with open("input/i18.txt") as f:
        for l in f:
            n.append(list(map(int, l.strip().split(','))))
    return m, n, sz

def bfs(m, sz):
    s, e = (1, 1), (sz, sz)
    q = deque([[s[0], s[1], 0]])
    d = {s: 0}
    while q:
        x, y, cost = q.popleft()
        if (x, y) == e:
            return d[e]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if m[nx][ny] == '.' and d.get((nx, ny), float('inf')) > cost + 1:
                d[(nx, ny)] = d[(x, y)] + 1
                q.append([nx, ny, cost + 1])
    return None

def part1():
    m, n, sz = read_input()
    for x, y in n[:1024]:
        m[x+1][y+1] = '#'
    print(bfs(m, sz))

def part2():
    m, n, sz = read_input()
    nn = len(n)
    lb, rb = 0, nn
    # Find the first n where the bfs fails.
    while lb < rb:
        mid = (lb + rb) // 2
        m2 = [r[:] for r in m]
        for x, y in n[:mid]:
            m2[x+1][y+1] = '#'
        if bfs(m2, sz) is None:
            rb = mid
        else:
            lb = mid + 1
    print(n[lb-1])

part1()
part2()
