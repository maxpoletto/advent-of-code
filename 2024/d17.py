from collections import deque
import re

def read_input():
    """Return map and start and end positions."""
    reg, prog = {}, []
    with open("input/i17.txt") as f:
        for l in f:
            if m := re.match(r"Register (\w): (\d+)$", l):
                reg[m.group(1)] = int(m.group(2))
            elif m := re.match(r"Program: ([\d,]+)", l):
                prog = list(map(int, m.group(1).split(',')))
    return reg, prog

def run(a, b, c, prog):
    def combo(n):
        assert n < 7
        return [n, n, n, n, a, b, c][n]
    i = 0
    res = []
    while i < len(prog):
        op = prog[i]
        v = prog[i+1] if i+1 < len(prog) else None
        match op:
            case 0: a = a >> combo(v)
            case 1: b = b ^ v
            case 2: b = combo(v) & 7
            case 3: i = v-2 if a != 0 else i
            case 4: b = b ^ c
            case 5: res.append(combo(v) & 7)
            case 6: b = a >> combo(v)
            case 7: c = a >> combo(v)
        i += 2
    return res

def explore():
    _, prog0 = read_input()
    prog1 = [0,3,5,4,3,0]
    prog2 = [2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0]
    for prog in [ prog0, prog1, prog2 ]:
        i = 1
        # Every multiplication by 8 shifts the output by 1.
        # Low-order bits control left values.
        while i <= 8**7:
            for j in range(32):
                res = run(i+j, 0, 0, prog)
                print(i+j, res)
            i *= 8

def find(prog):
    # Complexity is O(log_8(a) * n) where n is the length of the program.
    q = deque([[0, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]])
    while q:
        a, l = q.popleft()
        res = run(a, 0, 0, prog)
        if res == prog:
            return a
        if res == prog[-l:]:
            for i in range(8):
                q.append([a*8+i, l+1])

def part1():
    reg, prog = read_input()
    print(','.join(map(str, run(reg['A'], reg['B'], reg['C'], prog))))

def part2():
    _, prog = read_input()
    print(find(prog))

part1()
part2()
