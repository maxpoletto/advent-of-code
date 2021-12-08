from collections import defaultdict
from lib import aodfile

"""
7-segment display:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""

digits = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

def decode(patterns, output):
    freq = defaultdict(int) # map of segment frequencies
    for p in patterns:
        for c in p:
            freq[c] += 1
    code = {}

    # If an undecoded segment appears f times, it must map to segment v.
    def find_by_freq(f, v):
        for c in freq:
            if freq[c] == f and c not in code.keys():
                code[c] = v
                return
    # If a segment is the remaining undecoded segment in a pattern of length l,
    # it must map to segment v.
    def find_by_len(l, v):
        for p in patterns:
            if len(p) == l:
                for c in p:
                    if c not in code.keys():
                        code[c] = v
                        return

    # Segments e, b, and f occur a unique number of times.
    find_by_freq(4, 'e')
    find_by_freq(6, 'b')
    find_by_freq(9, 'f')
    # '1' is the only 2-segment digit. We know f, so find c.
    find_by_len(2, 'c')
    # '4' is the only 4-segment digit. We know b, c, and f, so find d.
    find_by_len(4, 'd')
    # d and g are the only segments that appear 7 times. We know d, find g.
    find_by_freq(7, 'g')
    # a and c are the only segments that appear 8 times. We know c, find a.
    find_by_freq(8, 'a')

    # Now decode the output digits.
    n = 0
    for digit in output:
        n *= 10
        decoded = ''
        for c in digit:
            decoded += code[c]
        n += digits[''.join(sorted(decoded))]
    return n

def part1():
    t = 0
    for l in aodfile.stripped_lines("input/input08.txt"):
        v = l.split('|')[1]
        for v2 in v.split():
            t += len(v2) == 2 or len(v2) == 7 or len(v2) == 3 or len(v2) == 4
    print(t)

def part2():
    tot = 0
    for l in aodfile.stripped_lines("input/input08.txt"):
        pat, out = l.split('|')[0].split(), l.split('|')[1].split()
        tot += decode(pat, out)
    print(tot)

part1()
part2()
