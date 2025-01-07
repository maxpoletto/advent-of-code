from collections import deque
import time

def read_input():
    """Return map and start and end positions."""
    m = []
    with open("input/i16.txt") as f:
        for l in f:
            m.append(list(l.strip()))
    s, e = None, None
    for i, r in enumerate(m):
        for j, c in enumerate(r):
            if c == "E":
                m[i][j] = '.'
                e = (i, j)
            elif c == "S":
                m[i][j] = '.'
                s = (i, j)
    return m, s, e

dirs = { '^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1) }
# Moves forward, left, right, and the corresponding costs
rot =  { '^': "^<>",   'v': "v><",  '<': "<v^",   '>': ">^v"  }
costs = [ 1, 1001, 1001 ]
INF = float('inf')

def least_cost(m, start, end, dir):
    """Find the least-cost path from s to e, heading in direction d."""
    score = { start: 0 }
    q = deque([[start, dir, 0]])
    while q:
        tile, dir, cost = q.popleft()
        if tile == end:
            continue
        for i in range(3): # forward, left, right
            ndir = rot[dir][i]
            ntile = (tile[0] + dirs[ndir][0], tile[1] + dirs[ndir][1])
            if m[ntile[0]][ntile[1]] == '#':
                continue
            ncost = cost + costs[i]
            if score.get(ntile, INF) > ncost:
                score[ntile] = ncost
                q.append([ntile, ndir, ncost])
    best = score[end]
    q = deque([[end, 'v', best],  # going down
               [end, '<', best]]) # going left
    seen = set({end})
    while q:
        tile, dir, cost = q.popleft()
        if tile == start:
            continue
        for i in range(3): # forward, left, right
            ndir = rot[dir][i]
            ntile = (tile[0] + dirs[ndir][0], tile[1] + dirs[ndir][1])
            ncost = cost - costs[i]
            ocost = score.get(ntile, INF)
            if (ocost == ncost or ocost == ncost-1000) and ntile not in seen:
                seen.add(ntile)
                q.append([ntile, ndir, ncost])
    return (best, len(seen))

def parts():
    m, s, e = read_input()
    t0 = time.time()
    print(least_cost(m, s, e, '>'))
    print("Elapsed = ", time.time() - t0)

parts()
