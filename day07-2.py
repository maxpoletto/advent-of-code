#!/opt/local/bin/python

import re

fn = "input07.txt"
r = re.compile(r'(\d+) ([a-z ]+?) bag')
contains = {}
with open(fn) as f:
    for l in f:
        l = l.strip()
        container, contained = l.split(" bags contain ")
        if container not in contains:
            contains[container] = []
        for c in r.findall(contained):
            contains[container].append((int(c[0]), c[1]))

def count(b):
    n = 1
    for c in contains[b]:
        n += c[0] * count(c[1])
    return n

print(count("shiny gold")-1)
