#!/opt/local/bin/python

from lib import util
import collections
import re

def exec(instr, m):
    p = 0
    while p >= 0 and p < len(instr):
        i = instr[p]
        if i[0] == 'jio':
            if m[i[1]] == 1:
                p += i[2]
                continue
        elif i[0] == 'jie':
            if m[i[1]] % 2 == 0:
                p += i[2]
                continue
        elif i[0] == 'jmp':
            p += i[1]
            continue
        elif i[0] == 'inc':
            m[i[1]] += 1
        elif i[0] == 'tpl':
            m[i[1]] *= 3
        elif i[0] == 'hlf':
            m[i[1]] = int(m[i[1]]/2)
        p += 1

def part1(instr):
    m = collections.defaultdict(int)
    exec(instr, m)
    return m['b']

def part2(instr):
    m = collections.defaultdict(int)
    m['a'] = 1
    exec(instr, m)
    return m['b']

fn = 'input/input23.txt'
instr = []
with open(fn) as f:
    for l in f:
        i = re.sub(r',', '', l).strip().split(' ')
        i[-1] = util.intorstr(i[-1])
        instr.append(i)
print(part1(instr))
print(part2(instr))
