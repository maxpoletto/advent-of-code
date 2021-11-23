#!/usr/local/bin/python

"""Helper functions for matrix operations."""

def col(m, n):
    return ''.join([ row[n] for row in m])

def row(m, n):
    return ''.join(m[n])

def set(m, r0, c0, r1, c1, v):
    for r in range(r0, r1+1):
        for c in range(c0, c1+1):
            m[r][c] = v

def matrixify(strs):
    m = []
    for s in strs:
        m.append([c for c in s])
    return m

def flip(v):
    v2 = []
    for i in range(len(v)-1,-1,-1):
        v2.append(v[i])
    return v2

# Rotate col c down by v
def rotate_col(m, c, v):
    l = len(m)
    t = [''] * l
    for i in range(l):
        t[(i+v)%l] = m[i][c]
    for i in range(l):
        m[i][c] = t[i]
    return m

# Rotate row r right by v
def rotate_row(m, r, v):
    l = len(m[r])
    t = [''] * l
    for i in range(l):
        t[(i+v)%l] = m[r][i]
    for i in range(l):
        m[r][i] = t[i]
    return m

def rotate(m):
    assert(len(m) == len(m[0]))
    l = len(m)
    m2 = [ [ None for x in range(l) ] for y in range(l) ]
    for r in range(l):
        for c in range(l):
            m2[l-1-c][r] = m[r][c]
    return m2

def pp(m):
    s = ""
    for l in m:
        s += ''.join(l) + "\n"
    return s

def test_transforms():
    m = [[1,2,3],[4,5,6],[7,8,9]]

    print(m)

    print()
    print(rotate_col(m, 0, 1))
    print(rotate_col(m, 1, 2))
    print(rotate_col(m, 0, 2))
    print(rotate_col(m, 1, 1))

    print()
    print(rotate_row(m, 1, 1))
    print(rotate_row(m, 1, 2))

    print()
    print(rotate(m))
    print(rotate(rotate(m)))
    print(rotate(rotate(rotate(m))))

    print()
    print(flip(m))
    print(rotate(flip(m)))
    print(rotate(rotate(flip(m))))
    print(rotate(rotate(rotate(flip(m)))))
