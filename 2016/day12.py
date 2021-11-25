from lib import aodfile

def exec(code, reg, m) -> int:
    def val(x):
        if x in m.keys():
            return m[x]
        else:
            return int(x)
    i = 0
    while i < len(code):
        c = code[i]
        if c[0] == 'cpy':
            m[c[2]] = val(c[1])
        elif c[0] == 'inc':
            m[c[1]] += 1
        elif c[0] == 'dec':
            m[c[1]] -= 1
        elif c[0] == 'jnz':
            if val(c[1]) != 0:
                i += int(c[2])
                continue
        i += 1
    return m[reg]

def part1():
    code = list(map(lambda x: x.split(), aodfile.stripped_lines("input/input12.txt")))
    print(exec(code, 'a', m = { 'a': 0, 'b': 0, 'c': 0, 'd': 0 }))

def part2():
    code = list(map(lambda x: x.split(), aodfile.stripped_lines("input/input12.txt")))
    print(exec(code, 'a', m = { 'a': 0, 'b': 0, 'c': 1, 'd': 0 }))

part1()
part2()
