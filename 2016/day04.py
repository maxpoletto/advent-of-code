import re
from lib import aodfile
from string import ascii_lowercase

def parse_room(s):
    m = re.match(r'([a-z\-]+)\-(\d+)\[([a-z]+)\]', s)
    assert(m)
    return m.group(1).strip('-'), int(m.group(2)), m.group(3)

def is_valid(name, checksum):
    x = list(map(lambda x: [x, 0], list(ascii_lowercase)))
    for c in name:
        if c in ascii_lowercase:
            x[ord(c)-ord('a')][1] += 1
    y = sorted(x, key=lambda x: (-x[1],x[0]))
    z = ''.join(map(lambda x: x[0], y[:len(checksum)]))
    return z == checksum

def rotate(name, i):
    rname = ""
    for c in name:
        if c == '-':
            rname += ' '
        else:
            x = (ord(c) - ord('a') + i) % 26
            rname += chr(ord('a') + x)
    return rname

def part1():
    lines = aodfile.stripped_lines("input/input04.txt")
    tot = 0
    for l in lines:
        name, id, checksum = parse_room(l)
        if is_valid(name, checksum):
            tot += id
    print(tot)

def part2():
    lines = aodfile.stripped_lines("input/input04.txt")
    for l in lines:
        name, id, checksum = parse_room(l)
        if is_valid(name, checksum):
            print(rotate(name, id), id)

part1()
part2()
