#!/opt/local/bin/python

import re

fn = "input07.txt"
r = re.compile(r'(\d+) ([a-z ]+?) bag')
contained_by = {}
with open(fn) as f:
    for l in f:
        l = l.strip()
        container, contained = l.split(" bags contain ")
        for c in r.findall(contained):
            if c[1] not in contained_by:
                contained_by[c[1]] = []
            contained_by[c[1]].append(container)

res = {}
def containers(b):
    if b not in contained_by:
        return
    for c in contained_by[b]:
        res[c] = True
        containers(c)

containers("shiny gold")
print(len(res))
