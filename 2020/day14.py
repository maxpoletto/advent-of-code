#!/usr/local/bin/python

import re

def val_mask(s):
    """Returns a new mask object for part 1:
    m[0] = significant bits, m[1] = bit values to overwrite.
    """
    m = [0,0]
    for c in s:
        m[0] <<= 1
        m[1] <<= 1
        if c == '0':
            m[0] |= 1
        elif c == '1':
            m[0] |= 1
            m[1] |= 1
    return m

def addr_mask(s):
    """Returns a new mask object for part 2:
    m[0] = 1 bits (to overwrite), m[1] = float bits
    """
    m = [0,0]
    for c in s:
        m[0] <<= 1
        m[1] <<= 1
        if c == '1':
            m[0] |= 1
        elif c == 'X':
            m[1] |= 1
    return m

def val(v, m):
    """Returns val_mask() m applied to value v."""
    return (v & ~m[0]) | m[1]

def addrs(v, m):
    """Returns addr_mask() m applied to value (address) v.
    Given k "float bits" in m, the result is an array of 2^k values in which
    all the 1 bits are set and the float bits take on all possible values.
    """
    r = [(v|m[0])&~m[1]] # 1 bits set to 1, float bits set to 0
    for i in range(0, 36): # 36-bit words
        b = m[1] & (1<<i)
        if b != 0:
            r2 = []
            for w in r:
                r2.append(w|b)
            r += r2
    return r

def test_value():
    print(val(11, val_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")))
    print(val(101, val_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")))
    print(val(0, val_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")))

def test_addresses():
    m = addr_mask("000000000000000000000000000000X1001X")
    print(addrs(42,m))
    m = addr_mask("00000000000000000000000000000000X0XX")
    print(addrs(26,m))

def part1(prog):
    mask, mem = [0, 0], {}
    for i in prog:
        if i[0] == 'mask':
            mask = val_mask(i[1])
        elif i[0] == 'set':
            mem[i[1]] = val(i[2], mask)
    sum = 0
    for m in mem:
        sum += mem[m]
    return sum

def part2(prog):
    mask, mem = [0, 0], {}
    for i in prog:
        if i[0] == 'mask':
            mask = addr_mask(i[1])
        elif i[0] == 'set':
            for a in addrs(i[1], mask):
                mem[a] = i[2]
    sum = 0
    for m in mem:
        sum += mem[m]
    return sum

fn = "input14.txt"
prog = []
with open(fn) as f:
    for l in f:
        m = re.match(r'mask = ([01X]+)', l)
        if m is not None:
            prog.append(['mask', m.group(1)])
            continue
        m = re.match(r'mem\[(\d+)\] = (\d+)', l)
        if m is not None:
            prog.append(['set', int(m.group(1)), int(m.group(2))])

print(part1(prog))
print(part2(prog))
