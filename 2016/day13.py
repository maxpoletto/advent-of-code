from collections import deque
from typing import Tuple

magic = 1364
wall = {}
def is_wall(p: Tuple) -> bool:
    if p in wall.keys():
        return wall[p]
    if p[0] < 0 or p[1] < 0:
        return True
    n = p[0]*(p[0] + 3 + 2*p[1]) + p[1]*(1 + p[1]) + magic
    o = bin(n).count('1')
    wall[p] = (o%2)==1
    return (o%2)==1

def shortest_path(p0, p1) -> int:
    visited = {}
    q = deque()
    q.append((p0, 0))
    while len(q) > 0:
        p, s = q.popleft()
        if p == p1:
            return s
        visited[p] = True
        for d in [ (-1,0), (1,0), (0,-1), (0,1)]:
            np = (p[0]+d[0], p[1]+d[1])
            if not is_wall(np) and not np in visited.keys():
                q.append((np, s+1))
    return -1

def num_locs(p0, n) -> int:
    visited = {}
    q = deque()
    q.append((p0, 0))
    while len(q) > 0:
        p, s = q.popleft()
        visited[p] = True
        if s == n:
            continue
        for d in [ (-1,0), (1,0), (0,-1), (0,1)]:
            np = (p[0]+d[0], p[1]+d[1])
            if not is_wall(np) and not np in visited.keys():
                q.append((np, s+1))
    return len(visited)

# part 1
print(shortest_path((1,1), (31,39)))
# part 2
print(num_locs((1,1), 50))
