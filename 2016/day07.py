import re
from lib import aodfile

def part1():
    lines = aodfile.stripped_lines("input/input07.txt")
    cnt = 0
    for l in lines:
        abba, nabba = 0, 0
        hyp = False
        for i in range(len(l)-3):
            if l[i] == '[':
                hyp = True
            elif l[i] == ']':
                hyp = False
            elif l[i] == l[i+3] and l[i] != l[i+1] and l[i+1] == l[i+2]:
                if hyp:
                    nabba += 1
                    break
                else:
                    abba += 1
        if abba > 0 and nabba == 0:
            cnt += 1
    print(cnt)

def part2():
    lines = aodfile.stripped_lines("input/input07.txt")
    cnt = 0
    for l in lines:
        aba, bab = {}, {}
        hyp = False
        for i in range(len(l)-2):
            if l[i] == '[':
                hyp = True
            elif l[i] == ']':
                hyp = False
            elif l[i] == l[i+2] and l[i] != l[i+1]:
                if hyp:
                    bab[l[i+1]+l[i]+l[i+1]] = True
                else:
                    aba[l[i:i+3]] = True
        for k in aba.keys():
            if k in bab.keys():
                cnt += 1
                break
    print(cnt)

part1()
part2()
