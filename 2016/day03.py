#!/usr/local/bin/python

from lib import aodfile

def part1():
    lines = aodfile.stripped_lines("input/input03.txt")
    vals = []
    valid = 0
    for l in lines:
        t = sorted(map(lambda x: int(x), l.split()))
        if t[0] + t[1] > t[2]:
            valid += 1
    print(valid)

def part2():
    lines = aodfile.stripped_lines("input/input03.txt")
    vals = [[],[],[]]
    for l in lines:
        t = list(map(lambda x: int(x), l.split()))
        for i in range(len(t)):
            vals[i].append(t[i])
    v = vals[0] + vals[1] + vals[2]
    i, valid = 0, 0
    while i < len(v):
        t = sorted(v[i:i+3])
        if t[0] + t[1] > t[2]:
            valid += 1
        i += 3
    print(valid)

part1()
part2()
