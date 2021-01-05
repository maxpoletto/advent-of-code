#!/opt/local/bin/python

import collections
import itertools
import re

def max_happiness(h):
    u = list(h.keys())
    m = 0
    # Do not permute one element (arbitrarily, the first) to eliminate
    # cyclic rotations. Len(u) speedup (n! -> (n-1)!).
    for t in itertools.permutations(u[1:]):
        s = 0
        t += (u[0],) # Add the first element back in.
        for i in range(len(t)):
            a,b = t[i], t[(i+1)%len(t)]
            s += h[a][b] + h[b][a]
        if s > m:
            m = s
    return m

def part1(h):
    return max_happiness(h)

def part2(h):
    h['me'] = {}
    for u in list(h.keys()):
        h['me'][u] = 0
        h[u]['me'] = 0
    return max_happiness(h)

fn = "input/input13.txt"
h = collections.defaultdict(dict)
with open(fn) as f:
    for l in f:
        m = re.match(r'(\w+) would (gain|lose) (\d+) .*next to (\w+)', l)
        v = int(m[3])
        if m[2] == 'lose':
            v = -v
        h[m[1]][m[4]] = v
print(part1(h))
print(part2(h))
