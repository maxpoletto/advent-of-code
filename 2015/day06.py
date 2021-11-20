#!/usr/local/bin/python

from lib import aodfile
import re

def part1(lines):
    m = [[False]*1000 for _ in range(1000)]
    for l in lines:
        t = l[0] == 'toggle'
        o = l[0] == 'turn on'
        for r in range(l[1],l[3]+1):
            for c in range(l[2],l[4]+1):
                m[r][c] = (t and not m[r][c]) or o
    n = 0
    for r in m:
        n += r.count(True)
    return n

def part2(lines):
    m = [[0]*1000 for _ in range(1000)]
    for l in lines:
        t = l[0] == 'toggle'
        o = l[0] == 'turn on'
        for r in range(l[1],l[3]+1):
            for c in range(l[2],l[4]+1):
                if t:
                    m[r][c] += 2
                elif o:
                    m[r][c] += 1
                else:
                    m[r][c] = max(m[r][c]-1, 0)
    n = 0
    for r in m:
        n += sum(r)
    return n

fn = "input/input06.txt"
lines = []
with open(fn) as f:
    for l in f:
        m = re.match(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', l)
        assert(m)
        lines.append([m.group(1),int(m.group(2)),int(m.group(3)),int(m.group(4)),int(m.group(5))])

print(part1(lines))
print(part2(lines))
