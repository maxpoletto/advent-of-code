from collections import Counter
from math import log2
import re

def read_input():
    p = re.compile(r'p=([\-\d]+),([\-\d]+) v=([\-\d]+),([\-\d]+)')
    robots = []
    with open("input/i14.txt") as f:
        for l in f:
            m = p.match(l)
            if m:
                robots.append([int(m.group(i)) for i in range(1, 5)])
    return robots

def move(nsec, nx, ny):
    robots = read_input()
    q = [ [0, 0], [0, 0] ]
    xmid, ymid = nx // 2, ny // 2
    for r in robots:
        r[0] = (r[0] + r[2] * nsec) % nx
        r[1] = (r[1] + r[3] * nsec) % ny
        if r[0] == xmid or r[1] == ymid:
            continue
        q[r[1] > ymid][r[0] > xmid] += 1
    print(q[0][0] * q[1][1] * q[0][1] * q[1][0])

def print_robots(robots, nx, ny):
    grid = [['.' for _ in range(nx)] for _ in range(ny)]
    for r in robots:
        grid[r[1]][r[0]] = '#'
    for row in grid:
        print(''.join(row))

INF = 1e9
def find_tree(nx, ny):
    robots = read_input()
    minq = INF
    for t in range(1, nx * ny):
        q = [ [0, 0], [0, 0] ]
        xmid, ymid = nx // 2, ny // 2
        for r in robots:
            r[0] = (r[0] + r[2]) % nx
            r[1] = (r[1] + r[3]) % ny
            if r[0] == xmid or r[1] == ymid:
                continue
            q[r[1] > ymid][r[0] > xmid] += 1
        qv = q[0][0] * q[1][1] * q[0][1] * q[1][0]
        if qv < minq:
            minq = qv
            print("-"*80, t, qv)
            print_robots(robots, nx, ny)

move(100, 101, 103) # Part 1
find_tree(101, 103) # Part 2
