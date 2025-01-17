from copy import deepcopy
from itertools import combinations
import re
def read_input():
    with open('input/input11.txt') as f:
        floors = []
        for l in f:
            floor = []
            for m in re.findall(r'(\w+)-compatible|(\w+) generator', l):
                if m[0]:
                    floor.append(m[0][:2].upper() + 'M')
                else:
                    floor.append(m[1][:2].upper() + 'G')
            floors.append(sorted(floor))
        return (0, floors)

def tostr(floors):
    return f'{floors[0]}|' + '|'.join(','.join(f) for f in floors[1]) + '|'
def fromstr(s):
    t = s.split('|')[:-1]
    return (int(t[0]), [x.split(',') for x in t[1:]])
def microchips(f):
    return [x for x in f if x[2] == 'M']
def generators(f):
    return [x for x in f if x[2] == 'G']
def chip_safe(f, c):
    return not generators(f) or any(x[:2] == c[:2] for x in generators(f))
def chip_atrisk(f, c):
    return c in f and any(x[:2] != c[:2] for x in generators(f))
def chip(g):
    return g[:2] + 'M'

def moves(s):
    e1, floors1 = fromstr(s)
    for e2 in (e1-1, e1+1):
        if e2 < 0 or e2 > 3:
            continue
        # Try moving microchips
        f1, f2 = floors1[e1], floors1[e2]
        for m1 in microchips(f1):
            for m2 in microchips(f1):
                if chip_safe(f2, m1):
                    floors2 = deepcopy(floors1)
                    floors2[e1].remove(m1)
                    floors2[e2].append(m1)
                    yield tostr((e2, floors2))
                if m1 != m2 and chip_safe(f2, m2):
                    floors2[e1].remove(m2)
                    floors2[e2].append(m2)
                    yield tostr((e2, floors2))
        # Try moving generators
        for g1 in generators(f1):
            for g2 in generators(f1):
                if not chip_atrisk(f2, chip(g1)):
                    floors2 = deepcopy(floors1)
                    floors2[e1].remove(g1)
                    floors2[e2].append(g1)
                    yield tostr((e2, floors2))
                if g1 != g2 and not chip_atrisk(f2, chip(g2)):
                    floors2[e1].remove(g2)
                    floors2[e2].append(g2)
                    yield tostr((e2, floors2))
        # Try moving microchips + generators in pairs
        for g in generators(f1):
            m = chip(g)
            if m in f1 and not chip_atrisk(f2, m):
                floors2 = deepcopy(floors1)
                floors2[e1].remove(g)
                floors2[e1].remove(m)
                floors2[e2].append(g)
                floors2[e2].append(m)
                yield tostr((e2, floors2))

def part1():
    e, floors = read_input()
    for s in moves(tostr((1, floors))):
        print(s)

part1()
