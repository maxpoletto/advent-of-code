#!/opt/local/bin/python

"""Helper functions for matrix operations."""

def col(m, n):
    return ''.join([ row[n] for row in m])

def row(m, n):
    return ''.join(m[n])

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

def rotate(m):
    assert(len(m) == len(m[0]))
    l = len(m)
    m2 = [ [ None for x in range(l) ] for y in range(l) ]
    for r in range(l):
        for c in range(l):
            m2[l-1-c][r] = m[r][c]
    return m2

def test_transforms():
    m = [[1,2,3],[4,5,6],[7,8,9]]
    print(m)
    print(rotate(m))
    print(rotate(rotate(m)))
    print(rotate(rotate(rotate(m))))

    print()
    print(flip(m))
    print(rotate(flip(m)))
    print(rotate(rotate(flip(m))))
    print(rotate(rotate(rotate(flip(m)))))
