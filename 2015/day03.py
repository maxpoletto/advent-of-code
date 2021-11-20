#!/usr/local/bin/python

from lib import aodfile

def move(p, d):
    if d == '^':
        return (p[0]-1, p[1])
    if d == 'v':
        return (p[0]+1, p[1])
    if d == '>':
        return (p[0], p[1]+1)
    if d == '<':
        return (p[0], p[1]-1)
    assert(False)

def count(h, p):
    if p in h:
        h[p] += 1
    else:
        h[p] = 1

def part1(dirs):
    h, p = {}, (0,0)
    h[p] = 1
    for d in dirs:
        p = move(p, d)
        count(h, p)
    return len(h)

def part2(dirs):
    h, px = {}, [(0,0), (0,0)]
    h[px[0]] = 2
    for j in range(len(dirs)):
        px[j%2] = move(px[j%2], dirs[j])
        count(h, px[j%2])
    return len(h)

fn = "input/input03.txt"
dirs = aodfile.stripped_text(fn)
print(part1(dirs))
print(part2(dirs))
