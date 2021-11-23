import re
from lib import aodfile

def part1():
    lines = aodfile.stripped_lines("input/input09.txt")
#    lines = aodfile.stripped_lines("x")

    cnt = 0
    for l1 in lines:
        pos = 0
        l2 = ""
        m = re.finditer('\((\d+)x(\d+)\)', l1)
        for g in m:
            lp, rp = g.start(), g.end()
            seqlen, seqcnt = int(g.group(1)), int(g.group(2))
            if lp < pos:
                continue
            l2 += l1[pos:lp] + l1[rp:rp+seqlen]*seqcnt
            pos = rp+seqlen
        if pos < len(l1):
            l2 += l1[pos:len(l1)]
        cnt += len(l2)
    print(cnt)

def part1():
    lines = aodfile.stripped_lines("input/input09.txt")
#    lines = aodfile.stripped_lines("x")

    cnt = 0
    for l1 in lines:
        pos = 0
        l2 = ""
        m = re.finditer('\((\d+)x(\d+)\)', l1)
        for g in m:
            lp, rp = g.start(), g.end()
            seqlen, seqcnt = int(g.group(1)), int(g.group(2))
            if lp < pos:
                continue
            l2 += l1[pos:lp] + l1[rp:rp+seqlen]*seqcnt
            pos = rp+seqlen
        if pos < len(l1):
            l2 += l1[pos:len(l1)]
        cnt += len(l2)
    print(cnt)

part1()
part2()
