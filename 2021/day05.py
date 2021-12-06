import re
from collections import defaultdict
from lib import aodfile

def overlap(only_vertical):
    def dir(val):
        if val > 0:
            return -1
        elif val == 0:
            return 0
        return 1
    lines = []
    for l in aodfile.stripped_lines("input/input05.txt"):
        m = re.match('(\d+),(\d+) -> (\d+),(\d+)',l)
        if m:
            lines.append(((int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))))
    m = defaultdict(int)
    for p1p2 in lines:
        if only_vertical and p1p2[0][0] != p1p2[1][0] and p1p2[0][1] != p1p2[1][1]:
            continue
        ix = dir(p1p2[0][0] - p1p2[1][0])
        iy = dir(p1p2[0][1] - p1p2[1][1])
        p = p1p2[0]
        #print("xxx", p1p2)
        while (True):
            m[p] += 1
            if p == p1p2[1]:
                break
            p = (p[0]+ix, p[1]+iy)
    n = 0
    for k in m.keys():
        if m[k] >= 2:
            n += 1
    print(n)

overlap(True)
overlap(False)
