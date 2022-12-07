from lib import aodfile

def part1():
    """read every line in input04.txt"""
    n = 0
    with open("input/input04.txt") as f:
        for l in f:
            l = l.strip()
            e1, e2 = l.split(',')
            e1 = [int(x) for x in e1.split('-')]
            e2 = [int(x) for x in e2.split('-')]
            if e1[0] >= e2[0] and e1[1] <= e2[1] or e1[0] <= e2[0] and e1[1] >= e2[1]:
                n += 1
    print(n)

def part2():
    n = 0
    with open("input/input04.txt") as f:
        for l in f:
            l = l.strip()
            e1, e2 = l.split(',')
            e1 = [int(x) for x in e1.split('-')]
            e2 = [int(x) for x in e2.split('-')]
            if not (e1[1] < e2[0] or e2[1] < e1[0]):
                n += 1
    print(n)

part1()
part2()
