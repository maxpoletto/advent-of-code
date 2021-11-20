#!/usr/local/bin/python

from lib import util
import re

def part1(repl, molec):
    m2 = {}
    for r in repl:
        for m in util.subiter(r[0], r[1], molec):
            m2[m] = True
    return len(m2.keys())

def part2(repl, molec):
    # Greedily replace the longest transformations first.
    repl.sort(key = lambda x: -len(x[1]))
    n = 0
    while molec != "e":
        for r in repl:
            (molec, n2) = re.subn(r[1], r[0], molec)
            n += n2
    return n

fn = "input/input19.txt"
repl = []
with open(fn) as f:
    for l in f:
        l = l.strip()
        m = re.match(r'(\w+) => (\w+)', l)
        if m:
            repl.append([m[1], m[2]])
            continue
        if len(l) > 0:
            molec = l

print(part1(repl, molec))
print(part2(repl, molec))
