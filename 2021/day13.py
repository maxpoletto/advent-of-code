import re
from collections import defaultdict
from collections import deque
from itertools import permutations
from lib import aodfile, mat

def part1():
    pts, folds = [], []
    xmax, ymax = 0, 0
    for l in aodfile.stripped_lines("input/input13.txt"):
        m = re.match('^(\d+),(\d+)$', l)
        if m:
            pts.append((int(m.group(1)), int(m.group(2))))
            xmax = max(xmax, pts[-1][0])
            ymax = max(ymax, pts[-1][1])
            continue
        m = re.match('fold along (.)=(\d+)', l)
        if m:
            folds.append((m.group(1), int(m.group(2))))
    h, w = ymax+1, xmax+1
    m = [ ['.'] * w  for i in range(h) ]
    for p in pts:
        m[p[1]][p[0]] = '#'
#    ndots = 0
    print('xxx', len(m), len(m[0]))
    for f in folds:
        if f[0] == 'x':
            print(f, len(m))
            ml, mr = [], []
            for r in m:
                assert(len(r) == 1+f[1]*2)
                ml.append(r[:f[1]])
                mr.append(r[f[1]+1:])
            mr = mat.mirror_h(mr)
            for i in range(len(ml)):
                for j in range(len(ml[0])):
                    if ml[i][j] == '#' or mr[i][j] == '#':
                        ml[i][j] = '#'
            m = ml
        elif f[0] == 'y':
            print(f, len(m))
            assert(len(m) == 1+f[1]*2)
            mt, mb = m[:f[1]], m[f[1]+1:]
            mb = mat.mirror_v(mb)
            for i in range(len(mt)):
                for j in range(len(mt[0])):
                    if mt[i][j] == '#' or mb[i][j] == '#':
                        mt[i][j] = '#'
            m = mt
    for r in m:
        print(''.join(r))

#                        ndots += 1
#    print(ndots)
def part2():
    return

part1()
part2()
