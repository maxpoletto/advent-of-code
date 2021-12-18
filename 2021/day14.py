import re
from collections import defaultdict
from collections import deque
from itertools import permutations
from copy import deepcopy
from lib import aodfile, mat

def step(src, rules):
    dst = src[0]
    for i in range(0, len(src)-1):
        t = src[i:i+2]
        dst += rules[t] + t[1]
    return dst

def part1():
    template = ""
    rules = defaultdict(str)
    for l in aodfile.stripped_lines("input/input14.txt"):
        m = re.match('^(\w+)$', l)
        if m:
            template = m.group(1)
            continue
        m = re.match('(\w\w) -> (\w)', l)
        if m:
            rules[m.group(1)] = m.group(2)
    for s in range(10):
        template = step(template, rules)
    freq = []
    for a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        freq.append(template.count(a))
    freq.sort()
    for i in range(len(freq)):
        if freq[i] > 0:
            break
    print(freq[-1]-freq[i])

def step2(freq, rules):
    f2 = deepcopy(freq)
    for s in freq:
        if s not in rules:
            continue
        f = freq[s]
        r1 = s[0] + rules[s]
        r2 = rules[s] + s[1]
        f2[r1] += f
        f2[r2] += f
        f2[s] -= f
    return f2

def part2():
    template = ""
    rules = defaultdict(str)
    for l in aodfile.stripped_lines("input/input14.txt"):
        m = re.match('^(\w+)$', l)
        if m:
            template = m.group(1)
            continue
        m = re.match('(\w\w) -> (\w)', l)
        if m:
            rules[m.group(1)] = m.group(2)
    freq = defaultdict(int)
    for i in range(len(template)-1):
        freq[template[i:i+2]] += 1
    print(freq)
    for s in range(40):
        freq = step2(freq, rules)
        print(freq)
    a = defaultdict(int)
    for s in freq:
        a[s[0]] += freq[s]
    l = min(a, key = lambda x:a[x])
    h = max(a, key = lambda x:a[x])
    print(a[h]-a[l]+1)

part1()
part2()
