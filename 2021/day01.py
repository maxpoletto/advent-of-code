from lib import aodfile

def part1():
    d = [int(x) for x in aodfile.stripped_lines("input/input01.txt")]
    n = 0
    for i in range(1, len(d)):
        if d[i] > d[i-1]:
            n += 1
    print(n)

def part2():
    d = [int(x) for x in aodfile.stripped_lines("input/input01.txt")]
    n = 0
    for i in range(1, len(d)-2):
        if d[i+1]+d[i+2] > d[i-1]+d[i+1]:
            n += 1
    print(n)
    return

part1()
part2()
