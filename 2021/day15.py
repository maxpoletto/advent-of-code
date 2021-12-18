from collections import deque
from lib import aodfile, pqueue

INF = 10000
NEIGHBORS = [(-1,0), (1,0), (0,-1), (0,1)]

def shortest_path(m, p1, p2):
    q = pqueue.PQueue()
    dist = {}
    dist[p1] = 0
    for y in range(1, len(m)-1):
        for x in range(1, len(m[0])-1):
            p = (x,y)
            if p != p1:
                dist[p] = INF
            q.add(p, dist[p])
    while not q.empty():
        u = q.pop()
        if u == p2:
            break
        for d in NEIGHBORS:
            v = (u[0]+d[0], u[1]+d[1])
            if not q.contains(v):
                continue
            alt = dist[u] + m[v[1]][v[0]]
            if alt < dist[v]:
                dist[v] = alt
                q.add(v, alt)
    return dist[p2]

def part1():
    m = []
    for l in aodfile.stripped_lines("input/input15.txt"):
        m.append([INF] + list(map(int, l)) + [INF])
    m = [ [INF] * len(m[0])] + m + [ [INF] * len(m[0])]
    print(shortest_path(m, (1,1), (len(m[0])-2,len(m)-2)))

def part2():
    n = []
    for l in aodfile.stripped_lines("input/input15.txt"):
        n.append(list(map(int, l)))
    h, w = len(n), len(n[0])
    m = [ [INF] * (2+5*w) for i in range(2+5*h) ]
    for r in range(h):
        for c in range(w):
            m[1+r][1+c] = n[r][c]
    for r in range(1,1+h):
        for c in range(1+w,1+5*w):
            m[r][c] = m[r][c-w]+1
            if m[r][c] > 9:
                m[r][c] = 1
    for r in range(1+h,1+5*h):
        for c in range(1,1+5*w):
            m[r][c] = m[r-w][c]+1
            if m[r][c] > 9:
                m[r][c] = 1
    print(shortest_path(m, (1,1), (len(m[0])-2,len(m)-2)))

part1()
part2()
