from copy import deepcopy

# Return a tuple (m, pos, cur), where m is the map, pos is the (row, col) position of the guard,
# and cur is the guard's current direction (one of the keys of the dir dictionary).
def read_input():
    # Returns 
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
    return m, pos, cur

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

# Advance the guard in the current direction, or turn if it hits an obstacle.
# Returns (None, None) if the guard goes out of bounds.
def advance(m, pos, cur):
    d = dir[cur]
    p2 = (pos[0] + d[0], pos[1] + d[1])
    if p2[0] < 0 or p2[0] >= len(m) or p2[1] < 0 or p2[1] >= len(m[0]):
        return None, None
    if m[p2[0]][p2[1]] != '.':
        cur = turn[cur]
    else:
        pos = p2
    return cur, pos

def part1():
    m, pos, cur = read_input()
    v = set()
    while (True):
        v.add(pos)
        cur, pos = advance(m, pos, cur)
        if not cur:
            break
    print(len(v))

def try_loop(m, v, pos, cur):
    obs = (pos[0] + dir[cur][0], pos[1] + dir[cur][1])

    # Do not place an obstacle (a) out of bounds, (b) where another obstacle
    # already exists, (c) where the guard has already walked (otherwise she
    # would not be able to reach the current spot).
    if (obs[0] < 0 or obs[0] >= len(m) or obs[1] < 0 or obs[1] >= len(m[0]) or
        m[obs[0]][obs[1]] != '.' or v[obs[0]][obs[1]] != '.'):
        return None

    m[obs[0]][obs[1]] = '#'
    cur = turn[cur]
    v2 = {}
    while (True):
        v2[pos] = v2.get(pos, 0) + 1
        cur, pos = advance(m, pos, cur)
        if not cur:
            m[obs[0]][obs[1]] = '.'
            return None
        # The obstacle creates a loop if (a) we find ourselves on
        # the previous path going in the same direction (v), or (b) we
        # have visited the same cell more than twice (v2). Case (a)
        # is a short-cut, but case (b) is necessary to detect
        # single-row/column loops (>>>> <<<<) in places the guard
        # has not visited before.
        if v[pos[0]][pos[1]] == cur or pos in v2 and v2[pos] > 2:
            m[obs[0]][obs[1]] = '.'
            return obs

def part2():
    m, pos, cur = read_input()
    v = deepcopy(m) # Map of the guard's path
    obs = set()
    while (True):
        d = dir[cur]
        v[pos[0]][pos[1]] = cur
        o = try_loop(m, v, pos, cur)
        if o:
            obs.add(o)
        p2 = (pos[0] + d[0], pos[1] + d[1])
        if p2[0] < 0 or p2[0] >= len(m) or p2[1] < 0 or p2[1] >= len(m[0]):
            break
        if m[p2[0]][p2[1]] != '.':
            cur = turn[cur]
            v[pos[0]][pos[1]] = cur
        else:
            pos = p2
    print(len(obs))

part1()
part2()
