#!/opt/local/bin/python

import re
import collections

def part1(v):
    v = int(v/10)
    h = [0]*(v+1)
    for d in range(1, v+1):
        for i in range(d, v+1, d):
            h[i] += d
    for i in range(1, v+1):
        if h[i] >= v:
            return i
    return -1

def part2(v):
    v = int(v/10)
    h = [0]*(v+1)
    for d in range(1, v+1):
        for i in range(d, min(v+1, d+d*49), d):
            h[i] += d*11
    for i in range(1, v+1):
        if h[i] >= v*10:
            return i
    return -1

print(part1(33100000))
print(part2(33100000))
