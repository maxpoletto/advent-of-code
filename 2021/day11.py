from collections import deque
from lib import aodfile

MIN = -1000
NEIGHBORS = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]

def step(m):
    nf = 0
    q = deque()
    for r in range(1, len(m)-1):
        for c in range(1, len(m[0])-1):
            if m[r][c] == 9:
                q.append((r,c))
                nf += 1
            m[r][c] += 1
    while len(q) > 0:
        r, c = q.popleft()
        for d in NEIGHBORS:
            r2, c2 = r+d[0],c+d[1]
            if m[r2][c2] == 9:
                q.append((r2,c2))
                nf += 1
            m[r2][c2] += 1
    for r in range(1, len(m)-1):
        for c in range(1, len(m[0])-1):
            if m[r][c] > 9:
                m[r][c] = 0
    return nf

def part1():
    m = []
    for l in aodfile.stripped_lines("input/input11.txt"):
        m.append([MIN] + list(map(int, l)) + [MIN])
    m = [ [MIN] * len(m[0])] + m + [ [MIN] * len(m[0])]
    nf = 0
    for i in range(100):
        nf += step(m)
    print(nf)

def part2():
    m = []
    for l in aodfile.stripped_lines("input/input11.txt"):
        m.append([MIN] + list(map(int, l)) + [MIN])
    m = [ [MIN] * len(m[0])] + m + [ [MIN] * len(m[0])]
    n = (len(m)-2)*(len(m[0])-2)
    i = 0
    while True:
        i += 1
        if step(m) == n:
            print(i)
            break

part1()
part2()
