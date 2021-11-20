#!/usr/local/bin/python
 
from functools import reduce
from itertools import combinations
from math import prod

p = [ 1, 2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43,
      53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113 ]

def best_entanglement(p, num_trunks):
    p = sorted(p, reverse = True)
    goal = sum(p)/num_trunks

    t, minlen = 0, 0
    for i in range(0, len(p)):
        t += p[i]
        if t >= goal:
            minlen = i+1
            break
    if minlen == 0:
        print("no combination")
        return        

    ents = []
    for n in range(minlen, len(p)+1):
        if len(ents) > 0:
            break
        for c in combinations(p, n):
            if sum(c) == goal:
                ents.append(prod(c))
    return sorted(ents)[0]

def part1():
    print(best_entanglement(p, 3))
def part2():
    print(best_entanglement(p, 4))

part1()
part2()

