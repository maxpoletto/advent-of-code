#!/usr/local/bin/python

import copy

def prepare(m):
    """Converts a list of strings describing a seating arrangement
    into a matrix, padded to eliminate boundary checks.
    """
    if len(m) == 0:
        return []
    w = len(m[0]) + 2
    n = [['.']*w]
    for r in m:
        n.append(['.'] + list(r) + ['.'])
    n.append(['.']*w)
    return n

def n_adj_occupied(m, r, c): 
    """Number of occupied seats adjacent to seat (r,c)."""
    n = 0
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if i == r and j == c:
                continue
            if m[i][j] == '#':
                n += 1
    return n 

def n_vis_occupied(m, r, c):
    """ Number of occupied seats separated from seat (r,c) only by empty floor,
    in any of 8 directions (N, NE, E, ...).
    """
    n = 0
    h, w = len(m), len(m[0])
    dirs = [[i,j] for i in [-1,0,1] for j in [-1,0,1] if i != 0 or j != 0]
    for d in dirs:
        i, j = r+d[0], c+d[1]
        while i > 0 and i < h and j > 0 and j < w:
            if m[i][j] == '#':
                n += 1
            if m[i][j] != '.':
                break
            i += d[0]
            j += d[1]
    return n

def tot_occupied(m):
    """Number of occupied seats in arrangement m."""
    n = 0
    for r in m:
        for c in r:
            if c == '#':
                n += 1
    return n

def shuffle(m, criterion, thresh):
    """Returns a shuffle of seating arrangement m given a visibility
    criterion and a minimum threshhold of visible seats.
    """
    m2 = copy.deepcopy(m)
    h, w = len(m), len(m[0])
    for r in range(1, h-1):
        for c in range(1, w-1):
            if m[r][c] == 'L' and criterion(m, r, c) == 0:
                m2[r][c] = '#'
            elif m[r][c] == '#' and criterion(m, r, c) >= thresh:
                m2[r][c] = 'L'
    return m2

def equal(m1, m2):
    if len(m1) != len(m2):
        return False
    h, w = len(m1), len(m1[0])
    for r in range(1, h-1):
        for c in range(1, w-1):
            if m1[r][c] != m2[r][c]:
                return False
    return True

def fixed_point(m, criterion, thresh):
    """Finds the fixed point of seating arrangement m given a visibility
    criterion and a minimum threshold of visible seats.
    """
    while True:
        m2 = shuffle(m, criterion, thresh)
        if equal(m, m2):
            return tot_occupied(m)
        m = m2
    return -1

def pp(m):
    """Pretty prints the seating arrangement, stripping border pads."""
    for r in range(1, len(m)-1):
        print(''.join(m[r][1:-1]))
    print()

def part1(m):
    return fixed_point(m, n_adj_occupied, 4)

def part2(m):
    return fixed_point(m, n_vis_occupied, 5)

fn = "input11.txt"
m = []
with open(fn) as f:
    for l in f:
        m.append(l.strip())

m = prepare(m)
print(part1(m))
print(part2(m))
