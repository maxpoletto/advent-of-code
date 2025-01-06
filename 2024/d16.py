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

dirs = [ (-1, 0), (0, 1), (1, 0), (0, -1) ] # clockwise order from up
costs = [ 1, 1001, 1001 ] # costs for going forward, left, right
INF = float('inf')

def least_cost(m, start, end, dirindex):
    """Find the least-cost path from start to end, heading in direction given by dirindex."""
    v = [ [ INF ] * len(m[0]) for _ in m ]
    v[start[0]][start[1]] = 0
    q = deque([[start[0], start[1], dirindex, 0]]) # tile, direction, cost
    while q:
        row, col, dir, cost = q.popleft()
        if (row, col) == end:
            continue
        # Directions are always enumerated in forward, left, right order
        newdirs = [ x % len(dirs) for x in [dir, dir-1, dir+1] ]
        for i, newdir in enumerate(newdirs):
            nrow, ncol = row + dirs[newdir][0], col + dirs[newdir][1]
            if m[nrow][ncol] == '#':
                continue
            ncost = cost + costs[i]
            if v[nrow][ncol] > ncost:
                v[nrow][ncol] = ncost
                q.append([nrow, ncol, newdir, ncost])

    best = v[end[0]][end[1]]
    q = deque([[end[0], end[1], 2, best],  # going down
               [end[0], end[1], 3, best]]) # going left
    seen = set({end})
    while q:
        row, col, dir, cost = q.popleft()
        if (row, col) == start:
            continue
        newdirs = [ x % len(dirs) for x in [dir, dir-1, dir+1] ]
        for i, newdir in enumerate(newdirs):
            nrow, ncol = row + dirs[newdir][0], col + dirs[newdir][1]
            ncost = cost - costs[i]
            if (v[nrow][ncol] == ncost or v[nrow][ncol] == ncost-1000) and (nrow, ncol) not in seen:
                seen.add((nrow, ncol))
                q.append([nrow, ncol, newdir, ncost])
    return (best, len(seen))

# Both parts
def parts():
    m, s, e = read_input()
    t0 = time.time()
    print(least_cost(m, s, e, 1))
    print("Elapsed = ", time.time() - t0)

parts()
