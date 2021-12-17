from collections import deque, defaultdict
from copy import deepcopy
from lib import aodfile

def ok(n, p):
    return (n[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or n not in p)

def ok2(n, p):
    if n[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or n not in p:
        return True
    if n in p and (n == 'start' or n == 'end'):
        return False
    for x in p:
        if x[0] in 'abcdefghijklmnopqrstuvwxyz':
            if p[x] > 1:
                return False
    return True

def num_paths(m, src, dst, path):
    if not ok2(src, path):
        return 0
    if src == dst:
        return 1
    np = 0
    path = deepcopy(path)
    path[src] += 1
    for src2 in m[src]:
        np += num_paths(m, src2, dst, path)
    return np

def part1():
    m = defaultdict(list)
    for l in aodfile.stripped_lines("input/input12.txt"):
        a,b = l.split('-')
        m[a].append(b)
        m[b].append(a)
    print(m)
    print(num_paths(m, 'start', 'end', defaultdict(int)))

def part2():
    return

part1()
part2()
