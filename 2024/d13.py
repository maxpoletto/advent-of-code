from math import lcm
import re

def read_input(offset = 0):
    ba = re.compile(r'Button A: X\+(\d+), Y\+(\d+)')
    bb = re.compile(r'Button B: X\+(\d+), Y\+(\d+)')
    pr = re.compile(r'Prize: X=(\d+), Y=(\d+)')
    res = []
    with open("input/i13.txt") as f:
        a, b, p = None, None, None
        for l in f:
            if ba.match(l):
                a = (int(ba.match(l).group(1)), int(ba.match(l).group(2)))
            elif bb.match(l):
                b = (int(bb.match(l).group(1)), int(bb.match(l).group(2)))
            elif pr.match(l):
                p = (int(pr.match(l).group(1)), int(pr.match(l).group(2)))
                res.append((a, b, (p[0]+offset, p[1]+offset)))
    return res

def calc(offset):
    machines = read_input(offset)
    tot_cost = 0
    for a, b, p in machines:
        nb = (p[0] * a[1] - p[1] * a[0]) // (a[1] * b[0] - a[0] * b[1])
        na = (p[1] - nb * b[1]) // a[1]
        if na * a[0] + nb * b[0] == p[0] and na * a[1] + nb * b[1] == p[1]:
            c = na * 3 + nb
            tot_cost += c
    print(tot_cost)

calc(0) # Part 1
calc(10000000000000) # Part 2
