from collections import deque
from lib import aodfile

def run_at_minima(func):
    hm = []
    for l in aodfile.stripped_lines("input/input09.txt"):
        hm.append([10] + list(map(int, l)) + [10])
    hm = [ [10] * len(hm[0])] + hm + [ [10] * len(hm[0])]
    for r in range(1, len(hm)-1):
        for c in range(1, len(hm[0])-1):
            low = True
            for d in [(-1,0), (1,0), (0,-1), (0,1)]:
                if hm[r+d[0]][c+d[1]] <= hm[r][c]:
                    low = False
                    break
            if low:
                func(hm, r, c)

def basin_size(m, r, c):
    q = deque()
    q.append((r,c))
    n = 0
    while len(q) > 0:
        r, c = q.popleft()
        if m[r][c] >= 9:
            continue
        n += 1
        m[r][c] = 10
        for d in [(-1,0), (1,0), (0,-1), (0,1)]:
            q.append((r+d[0], c+d[1]))
    return n

def part1():
    risk = 0
    def f(m, r, c):
        nonlocal risk
        risk += m[r][c]+1
    run_at_minima(f)
    print(risk)

def part2():
    basins = []
    def f(m, r, c):
        nonlocal basins
        basins.append(basin_size(m, r, c))
    run_at_minima(f)
    basins.sort(reverse=True)
    print(basins[0] * basins[1] * basins[2])

part1()
part2()
