#!/opt/local/bin/python

import itertools

def part1(x):
    i = 0
    for n in range(1, len(x)+1):
        for c in itertools.combinations(x,n):
            if sum(c) == 150:
                i += 1
    return i

def part2(x):
    i = 0
    for n in range(1, len(x)+1):
        for c in itertools.combinations(x,n):
            if sum(c) == 150:
                i+=1
        if i > 0:
            break
    return i

with open('2015/input/input17.txt') as f:
    x = [int(x) for x in f.readlines()]
print(part1(x))
print(part2(x))
