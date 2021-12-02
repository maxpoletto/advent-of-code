from lib import aodfile

def part1():
    insts = []
    for l in aodfile.stripped_lines("input/input02.txt"):
        v = l.split()
        insts.append((v[0], int(v[1])))
    hp, d = 0, 0
    for i in insts:
        if i[0] == 'forward':
            hp += i[1]
        elif i[0] == 'up':
            d -= i[1]
        elif i[0] == 'down':
            d += i[1]
    print(d*hp)

def part2():
    insts = []
    for l in aodfile.stripped_lines("input/input02.txt"):
        v = l.split()
        insts.append((v[0], int(v[1])))
    hp, d, aim = 0, 0, 0
    for i in insts:
        if i[0] == 'forward':
            hp += i[1]
            d += aim*i[1]
        elif i[0] == 'up':
            aim -= i[1]
        elif i[0] == 'down':
            aim += i[1]
    print(d*hp)

part1()
part2()
