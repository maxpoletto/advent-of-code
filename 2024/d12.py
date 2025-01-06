from collections import deque
from typing import Counter as CounterType

def read_input():
    m = []
    with open("input/i12.txt") as f:
        for l in f:
            m.append(['.'] + list(l.strip()) + ['.'])
    m.insert(0, ['.'] * len(m[0]))
    m.append(['.'] * len(m[0]))
    return m

def part1():
    m = read_input()
    regions = []
    visited = set()
    for r in range(1, len(m)-1):
        for c in range(1, len(m[0])-1):
            if (r, c) in visited:
                continue
            v, q = m[r][c], [(r, c)]
            area, peri = 0, 0
            visited.add((r, c))
            while q:
                rr, cc = q.pop(0)
                area += 1
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if m[rr+dr][cc+dc] != v:
                        peri += 1 
                    elif (rr+dr, cc+dc) not in visited:
                        visited.add((rr+dr, cc+dc))
                        q.append((rr+dr, cc+dc))
            regions.append((v, area, peri))
    print(sum(a*p for _, a, p in regions))

def part2():
    m = read_input()
    regions = []
    visited = set()
    for r in range(1, len(m)-1):
        for c in range(1, len(m[0])-1):
            if (r, c) in visited:
                continue
            v, q = m[r][c], deque({(r, c)})
            area, corn = 0, 0
            visited.add((r, c))
            while q:
                rr, cc = q.pop()
                area += 1
                for x, y in [(( 0,  1), (-1, 0)),  # upper right
                             (( 0,  1), ( 1, 0)),  # lower right
                             (( 0, -1), ( 1, 0)),  # lower left
                             (( 0, -1), (-1, 0))]: # upper left
                    if m[rr+x[0]][cc+x[1]] != v and m[rr+y[0]][cc+y[1]] != v:
                        # convex corner
                        corn += 1
                    elif (m[rr+x[0]][cc+x[1]] == v and m[rr+y[0]][cc+y[1]] == v and
                        m[rr+x[0]+y[0]][cc+x[1]+y[1]] != v):
                        # concave corner
                        corn += 1
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if m[rr+dr][cc+dc] == v and (rr+dr, cc+dc) not in visited:
                        visited.add((rr+dr, cc+dc))
                        q.append((rr+dr, cc+dc))
            regions.append((v, area, corn))
    print(sum(a*c for _, a, c in regions))

part1()
part2()
