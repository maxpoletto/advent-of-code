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

INF = float('inf')

def least_cost_hash(m, start, end, dir):
    """Find least cost path from start to end, starting in direction dir, using hash table to store costs."""

    dirs = { '^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1) }
    # Moves forward, left, right, and the corresponding costs
    rot =  { '^': "^<>",   'v': "v><",  '<': "<v^",   '>': ">^v"  }
    costs = [ 1, 1001, 1001 ]

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

def least_cost_grid(m, start, end, dirindex):
    """Find least cost path from start to end, starting in direction given by dirindex, using a grid to store costs."""

    dirs = [ (-1, 0), (0, 1), (1, 0), (0, -1) ] # clockwise order from up
    costs = [ 1, 1001, 1001 ] # costs for going forward, left, right

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
    print(least_cost_hash(m, s, e, '>'))
    print("Elapsed (hash) = ", time.time() - t0)
    t0 = time.time()
    print(least_cost_grid(m, s, e, 1))
    print("Elapsed (grid) = ", time.time() - t0)

parts()
