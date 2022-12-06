from lib import aodfile

def part1():
    wins = {
        'X': 'C', # rock beats scissors
        'Y': 'A', # paper beats rock
        'Z': 'B', # scissors beats paper
    }
    draws = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C',
    }
    value = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    with open("input/input02.txt") as f:
        pts = 0
        for l in f:
            v = l.strip().split()
            s, d = v[0], v[1]
            if s == draws[d]:
                pts += 3
            elif s == wins[d]:
                pts += 6
            pts += value[d]
    print(pts)

def part2():
    strat = {
        'X': { 'A': 'Z', 'B': 'X', 'C': 'Y' },
        'Y': { 'A': 'X', 'B': 'Y', 'C': 'Z' },
        'Z': { 'A': 'Y', 'B': 'Z', 'C': 'X' },
    }
    points = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }
    value = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    with open("input/input02.txt") as f:
        pts = 0
        for l in f:
            v = l.strip().split()
            pts += points[v[1]]
            pts += value[strat[v[1]][v[0]]]
    print(pts)

part1()
part2()
