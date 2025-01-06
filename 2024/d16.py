from collections import deque
# 577 too low
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

dirs = { # coordinate changes based on current direction
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}
rot = { # new directions based on current direction
    '^': "^<>",
    'v': "v><",
    '<': "<v^",
    '>': ">^v"
}
costs = [ 1, 1001, 1001 ] # costs for going forward, left, right, back
INF = float('inf')

def least_cost(m, s, e, d):
    """Find the least-cost path from s to e, heading in direction d."""
    q = deque([s])
    score, bestd = { s: 0 }, { s: '>' }
    bt = {}
    while q:
        n = q.pop()
        if n == e:
            continue
        d = bestd[n]
        for i in range(3): # forward, left, right
            nd = rot[d][i]
            g = (n[0] + dirs[nd][0], n[1] + dirs[nd][1])
            if m[g[0]][g[1]] == '#':
                continue
            cost = score[n] + costs[i]
            if score.get(g, INF) > cost:
                score[g], bestd[g] = cost, nd
                q.append(g)
                bt.setdefault(g, []).append([ n, score[n] ])

    best = score[e]

    # Backtrack to find the path
    tiles = set()
    # Find all paths back from e to s, and sum their costs
    # For each path, if the sum of the costs is is the best cost, add
    # all nodes in the path to the best set.
    q = deque([[e, best, [e]]])
    while q:
        n, cost, path = q.pop()
        print(n, cost)
        if n == s:
            print(path)
            tiles.update(path)
            continue
        for n2, c in bt[n]:
            if c in [cost - 1, cost - 1001] and n2 not in path:
                q.append([n2, c, path + [n2]])

    return best, len(tiles)

def part1():
    m, s, e = read_input()
    print(least_cost(m, s, e, '>'))

part1()
