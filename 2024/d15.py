from time import sleep

def read_input():
    m, cmds = [], ""
    with open("input/i15.txt") as f:
        for l in f:
            if len(l) == 0:
                continue
            if l[0] == '#':
                m.append(list(l.strip()))
            else:
                cmds += l.strip()
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == '@':
                return m, cmds, r, c

def widen(m):
    n = []
    for r in m:
        p = []
        for c in r:
            if c == '#':
                p.append('#')
                p.append('#')
            elif c == 'O':
                p.append('[')
                p.append(']')
            elif c == '.':
                p.append('.')
                p.append('.')
            else: # @
                p.append('@')
                p.append('.')
        n.append(p)
    for r in range(len(n)):
        for c in range(len(n[r])):
            if n[r][c] == '@':
                return n, r, c

def print_board(m, r, c):
    m[r][c] = '@'
    for row in m:
        print("".join(row))
    m[r][c] = '.'

dir = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

def part1():
    m, cmds, r, c = read_input()
    m[r][c] = '.'
    for cmd in cmds:
        r2, c2 = r + dir[cmd][0], c + dir[cmd][1]
        if m[r2][c2] == '#':
            continue
        if m[r2][c2] == '.':
            r, c = r2, c2
            continue
        assert m[r2][c2] == 'O'
        r3, c3 = r2, c2
        while m[r3][c3] == 'O':
            r3, c3 = r3 + dir[cmd][0], c3 + dir[cmd][1]
        if m[r3][c3] == '#':
            continue
        else:
            assert m[r3][c3] == '.'
            m[r3][c3] = 'O'
            m[r2][c2] = '.'
            r, c = r2, c2
    s = 0
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == 'O':
                s += r * 100 + c
    print(s)

VERBOSE = False
def part2():
    m, cmds, _, _ = read_input()
    m, r, c = widen(m)
    m[r][c] = '.'
    for cmd in cmds:
        r2, c2 = r + dir[cmd][0], c + dir[cmd][1]
        if VERBOSE:
            print_board(m, r, c)
            print(cmd)
            sleep(0.1)
        if m[r2][c2] == '#':
            continue
        if m[r2][c2] == '.':
            r, c = r2, c2
            continue
        assert m[r2][c2] in '[]'
        if cmd in '<>':
            r3, c3 = r2, c2
            while m[r3][c3] in '[]':
                r3, c3 = r3 + dir[cmd][0], c3 + dir[cmd][1]
            if m[r3][c3] == '#':
                continue
            assert m[r3][c3] == '.'
            for c4 in range(c3, c2, -dir[cmd][1]):
                m[r2][c4] = m[r2][c4 - dir[cmd][1]]
            m[r2][c2] = '.'
            r, c = r2, c2
        else: # ^v
            bl = c2-1 if m[r2][c2] == ']' else c2
            if can_move(m, r2, bl, dir[cmd][0]):
                move(m, r2, bl, dir[cmd][0])
                r, c = r2, c2
    print_board(m, r, c)
    s = 0
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == '[':
                s += r * 100 + c
    print(s)

# Returns true if the box [] with left bracket at (r, l) can be moved
# in direction dir (up or down).
def can_move(m, r, l, dir):
    r2 = r + dir
    if m[r2][l] == '#' or m[r2][l+1] == '#': # wall
        return False
    if m[r2][l] == '.' and m[r2][l+1] == '.': # empty space
        return True
    if m[r2][l] == '[' and m[r2][l+1] == ']':
        return can_move(m, r2, l, dir)
    if m[r2][l] == ']':
        assert m[r2][l-1] == '['
        if not can_move(m, r2, l-1, dir):
            return False
    if m[r2][l+1] == '[':
        assert m[r2][l+2] == ']'
        if not can_move(m, r2, l+1, dir):
            return False
    return True

# Moves the box [] with left bracket at (r, l) in direction dir (up or down).
# Requires that can_move(m, r, l, dir) is true.
def move(m, r, l, dir):
    r2 = r + dir
    assert m[r2][l] != '#' and m[r2][l+1] != '#' # Due to can_move()
    if m[r2][l] == '[' and m[r2][l+1] == ']':
        move(m, r2, l, dir)
    else:
        if m[r2][l] == ']':
            move(m, r2, l-1, dir)
        if m[r2][l+1] == '[':
            move(m, r2, l+1, dir)
    assert m[r2][l] == '.' and m[r2][l+1] == '.'
    m[r2][l], m[r2][l+1] = m[r][l], m[r][l+1]
    m[r][l], m[r][l+1] = '.', '.'

part1()
part2()
