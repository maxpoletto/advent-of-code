import re
from lib import aodfile
from string import ascii_lowercase

def part1():
    lines = aodfile.stripped_lines("input/input06.txt")
    cnt = [ list(map(lambda x: [x, 0], ascii_lowercase)) for x in range(len(lines[0]))]
    for l in lines:
        for i in range(len(l)):
            cnt[i][ord(l[i])-ord('a')][1] += 1
    sort_dec = map(lambda x: sorted(x, key=lambda y: -y[1]), cnt)
    res = ''.join(map(lambda x: x[0][0], sort_dec))
    print(res)

def part2():
    lines = aodfile.stripped_lines("input/input06.txt")
    cnt = [ list(map(lambda x: [x, 0], ascii_lowercase)) for x in range(len(lines[0]))]
    for l in lines:
        for i in range(len(l)):
            cnt[i][ord(l[i])-ord('a')][1] += 1
    no_zeros = map(lambda x: filter(lambda y: y[1] > 0, x), cnt)
    sort_inc = map(lambda x: sorted(x, key=lambda y: y[1]), no_zeros)
    res = ''.join(map(lambda x: x[0][0], sort_inc))
    print(res)

part1()
part2()
