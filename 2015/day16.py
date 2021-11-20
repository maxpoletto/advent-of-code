#!/usr/local/bin/python

import re
import collections

want = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

def part1(sue):
    for s in sue:
        ok = True
        for k in want:
            ok = k not in sue[s] or sue[s][k] == want[k]
            if not ok:
                break
        if ok:
            return s
    return -1

def part2(sue):
    for s in sue:
        ok = True
        for k in want:
            if k not in sue[s]:
                continue
            if k == 'cats' or k == 'trees':
                ok = sue[s][k] > want[k]
            elif k == 'pomeranians' or k == 'goldfish':
                ok = sue[s][k] < want[k]
            else:
                ok = sue[s][k] == want[k]
            if not ok:
                break
        if ok:
            return s
    return -1

fn = "input/input16.txt"
sue = collections.defaultdict(dict)
with open(fn) as f:
    i = 1
    for l in f:
        for c in re.findall(r'(\w+): (\d+)', l):
            sue[i][c[0]] = int(c[1])
        i += 1

print(part1(sue))
print(part2(sue))
