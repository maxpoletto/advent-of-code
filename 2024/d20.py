import heapq
from collections import Counter, deque

def read_input():
    m = []
    with open("input/i20.txt") as f:
        for l in f:
            if l.strip():
                m.append(['#'] + list(l.strip()) + ['#'])
    m = [['#'] * len(m[0])] + m + [['#'] * len(m[0])]
    start, end = None, None
    for i, r in enumerate(m):
        for j, c in enumerate(r):
            if c == 'S':
                start = (i, j)
                m[i][j] = '.'
            elif c == 'E':
                end = (i, j)
                m[i][j] = '.'
    return m, start, end

def neighbors(m, v):
    i, j = v
    for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if m[ni][nj] != '#':
            yield (ni, nj)

delta = [(-2, 0), (-1, -1), (-1, 1), (0, -2), (0, 2), (1, -1), (1, 1), (2, 0)]
def cheat_neighbors(m, v, radius):
    i, j = v
    if radius == 2: # special case for part 1
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if m[ni][nj] != '#':
                yield (ni, nj), 2
        return
    for di in range(-radius, radius+1):
        for dj in range(-radius, radius+1):
            if abs(di) + abs(dj) > radius or di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 2 <= ni < len(m) - 2 and 2 <= nj < len(m[0]) - 2 and m[ni][nj] != '#': 
                yield ((ni, nj), abs(di) + abs(dj))

def shortest_path(m, start, end):
    q = deque([[start, 0, [start]]])
    seen = {start}
    while q:
        u, d, path = q.popleft()
        if u == end:
            return path
        for ni, nj in neighbors(m, u):
            if (ni, nj) not in seen:
                seen.add((ni, nj))
                q.append([(ni, nj), d + 1, path + [(ni, nj)]])

def dijkstra(m, v):
    q = [(0, v)]
    dist = {v: 0}
    while q:
        d, u = heapq.heappop(q)
        if u in dist and dist[u] < d:
            continue
        for w in neighbors(m, u):
            if w in dist and dist[w] <= d + 1:
                continue
            dist[w] = d + 1
            heapq.heappush(q, (d + 1, w))
    return dist

def cheat(radius):
    m, start, end = read_input()
    path = shortest_path(m, start, end)
    dist = dijkstra(m, end)
    cheats = Counter()
    margin = 100
    for l, s in enumerate(path):
        for n, d in cheat_neighbors(m, s, radius):
            diff = (len(path) - l - 1) - (dist[n] + d)
            if diff >= margin:
                cheats[diff] += 1
    print(sum(cheats.values()))

cheat(2)  # part 1
cheat(20) # part 2
