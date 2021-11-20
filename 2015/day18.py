#!/usr/local/bin/python

from lib import aodfile, life

def part1(m):
    w = life.Bounded2D(m)
    w.step(100)
    return w.nactive()

def part2(m):
    w = life.Bounded2D(m)
    l = len(m)-1
    w.set(0, 0)
    w.set(l, 0)
    w.set(0, l)
    w.set(l, l)
    for _ in range(100):
        w.step(1)
        w.set(0, 0)
        w.set(l, 0)
        w.set(0, l)
        w.set(l, l)
    return w.nactive()

fn = 'input/input18.txt'
m = aodfile.stripped_lines(fn)
print(part1(m))
print(part2(m))
