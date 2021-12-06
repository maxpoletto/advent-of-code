import re
from collections import defaultdict
from collections import deque
from itertools import permutations
from lib import aodfile

def part1():
    insts = []
    for l in aodfile.stripped_lines("input/input03.txt"):
        v = l.split()
        insts.append((v[0], int(v[1])))

def part2():
    return

part1()
part2()
