from lib import aodfile

def part1():
    maxelf = 0
    elf = []
    with open("input/input01.txt") as f:
        for l in f:
            l = l.strip()
            if len(l) == 0:
                s = sum(elf)
                if s > maxelf:
                    maxelf = s
                elf = []
            else:
                elf.append(int(l))
    print(maxelf)

def part2():
    maxelves = []
    elf = []
    with open("input/input01.txt") as f:
        for l in f:
            l = l.strip()
            if len(l) == 0:
                s = sum(elf)
                if len(maxelves) < 3:
                    maxelves.append(s)
                    maxelves.sort()
                elif s > maxelves[0]:
                    maxelves[0] = s
                    maxelves.sort()
                elf = []
            else:
                elf.append(int(l))
            print(maxelves)
    print(sum(maxelves))

part1()
part2()
