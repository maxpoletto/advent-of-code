from lib import aodfile

def pri(c):
    if c >= 'a' and c <= 'z':
        return ord(c) - ord('a') + 1
    if c >= 'A' and c <= 'Z':
        return ord(c) - ord('A') + 27

def part1():
    pts = 0
    with open("input/input03.txt") as f:
        for l in f:
            l = l.strip()
            s = int(len(l)/2)
            h = {}
            for c in l[0:s]:
                h[c] = True
            for c in l[s:]:
                if c in h:
                    pts += pri(c)
                    del h[c]
    print(pts)

def part2():
    pts = 0
    l = aodfile.stripped_lines("input/input03.txt")
    for i in range(0, len(l), 3):
        h = {}
        for c in l[i]:
            h[c] = 1
        for c in l[i+1]:
            if c in h:
                h[c] = 2
        for c in l[i+2]:
            if c in h and h[c] == 2:
                pts += pri(c)
                break
    print(pts)

part1()
part2()
