#!/opt/local/bin/python

import itertools
import re

def make_graph(dists):
    g = {}
    for d in dists:
        if d[0] not in g:
            g[d[0]] = {}
        if d[1] not in g:
            g[d[1]] = {}
        g[d[0]][d[1]] = int(d[2])
        g[d[1]][d[0]] = int(d[2])
    return (g, list(g.keys()))

def part1(dists):
    g, cities = make_graph(dists)
    min_dist, min_path = 1<<31, []
    for path in itertools.permutations(cities):
        dist = 0
        for i in range(len(path)-1):
            dist += g[path[i]][path[i+1]]
        if dist < min_dist:
            min_dist = dist
            min_path = path
    return (min_dist, min_path)

def part2(dists):
    g, cities = make_graph(dists)
    max_dist, max_path = 0, []
    for path in itertools.permutations(cities):
        dist = 0
        for i in range(len(path)-1):
            dist += g[path[i]][path[i+1]]
        if dist > max_dist:
            max_dist = dist
            max_path = path
    return (max_dist, max_path)

fn = "input/input09.txt"
dist = []
with open(fn) as f:
    for l in f:
        dist.append(re.findall(r'(\w+) to (\w+) = (\d+)', l)[0])
print(part1(dist))
print(part2(dist))
