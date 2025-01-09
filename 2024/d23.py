import copy

def read_input():
    g = {}
    with open('input/i23.txt') as f:
        for line in f:
            a, b = line.strip().split('-')
            g.setdefault(a, set()).add(b)
            g.setdefault(b, set()).add(a)
    return g

def clique3(g):
    cliques = set()
    for n1, neighbors in g.items():
        if len(neighbors) < 2:
            continue
        for n2 in neighbors:
            neighbors2 = g[n2]
            for n3 in neighbors & neighbors2:
                cliques.add(frozenset([n1, n2, n3]))
    return cliques

def max_clique(g):
    g = copy.deepcopy(g)
    mq = set()
    for n in g:
        clique = set([n])
        for v in g:
            if v != n and all(v in g[u] for u in clique):
                clique.add(v)
        if len(clique) > len(mq):
            mq = clique
    return mq

def part1():
    cliques = clique3(read_input())
    print(sum(1 for c in cliques if any(n[0] == 't' for n in c)))

def part2():
    mq = max_clique(read_input())
    print(','.join(sorted([c for c in mq])))

part1()
part2()
