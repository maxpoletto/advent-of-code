#!/opt/local/bin/python

import re

fn = "input07.txt"
r = re.compile(r'(\d+) ([a-z ]+?) bag')
contains, contained_by = {}, {}
with open(fn) as f:
    for l in f:
        l = l.strip()
        container, contained = l.split(" bags contain ")
        if container not in contains:
            contains[container] = []
        for c in r.findall(contained):
            contains[container].append((int(c[0]), c[1]))
            if c[1] not in contained_by:
                contained_by[c[1]] = []
            contained_by[c[1]].append(container)

def containers_of(b, res):
    if b not in contained_by:
        return
    for c in contained_by[b]:
        res[c] = True
        containers_of(c, res)

def num_bags_in(b):
    n = 1
    for c in contains[b]:
        n += c[0] * num_bags_in(c[1])
    return n

def part1():
    res = {}
    containers_of("shiny gold", res)
    return len(res)

def part2():
    return num_bags_in("shiny gold")-1

print(part1())
print(part2())
