#!/opt/local/bin/python

import copy
import math
import re

def vert_edge(tile, n):
    return ''.join([ row[n] for row in tile])

def flip(s):
    s2 = ""
    for c in s:
        s2 = c+s2
    return s2

def flipv(v):
    v2 = [None] * len(v)
    for i in range(len(v)):
        v2[i] = v[len(v)-1-i]
    return v2

def mvflip(v):
    v2 = []
    for i in range(len(v)):
        v2.append(flipv(v[i]))
    return v2

def mhflip(v):
    v2 = []
    for i in range(len(v)-1,-1,-1):
        v2.append(v[i])
    return v2

def rotations(v):
    rots = [v]
    for _ in range(0, 3):
        v = v[1:] + v[:1]
        v = [ v[0], flip(v[1]), v[2], flip(v[3])]
        rots.append(v)
    return rots

"""
[0,2] -> [0,0]
[0,1] -> [1,0]
[0,0] -> [2,0]

[2,2] -> [0,2]
[1,2] -> [0,1]
[0,2] -> [0,0]

[0,0] -> [2,0]
[1,0] -> [2,1]
[2,0] -> [2,2]

123
456
789

369
258
147
"""

def rotate_matrix(m):
    assert(len(m) == len(m[0]))
    h = len(m)
    w = len(m[0])
    m2 = [ [ None for x in range(h) ] for y in range(w) ]
    for r in range(h):
        for c in range(w):
            m2[w-1-c][r] = m[r][c]
#            m2[0][1] = m[1][2]
    return m2

class Tile(object):
    def __init__(self, id, lines):
        self.id = id
        self.l = lines
        t = lines[0]
        b = lines[-1]
        l = vert_edge(lines, 0)
        r = vert_edge(lines, len(lines[0])-1)
        ft = flip(lines[0])
        fb = flip(lines[-1])
        fl = flip(vert_edge(lines, 0))
        fr = flip(vert_edge(lines, len(lines[0])-1))
        rot = rotations([t,r,b,l])
        rot += rotations([ft,l,fb,r]) # flipped around vertical axis
        rot += rotations([b,fr,t,fl]) # flipped around horizontal axis
        self.rotations = rot
        self.orientation = 0
    def top(self):
        return self.rotations[self.orientation][0]
    def right(self):
        return self.rotations[self.orientation][1]
    def bottom(self):
        return self.rotations[self.orientation][2]
    def left(self):
        return self.rotations[self.orientation][3]
    def num_orientations(self):
        return len(self.rotations)
    def orient(self, o):
        self.orientation = o
    def num_lines(self):
        return len(self.l)
    def image(self, cropped = True):
        res = []
        if cropped:
            for i in range(1, len(self.l)-1):
                res.append([ c for c in self.l[i][1:-1]])
        else:
            for i in range(len(self.l)):
                res.append([ c for c in self.l])
        o = self.orientation
        if o & 0x8: # flip around vertical axis
            res = mvflip(res)
        elif o & 0x4: # flip around horizontal axis
            res = mhflip(res)
        nrot = o & 0x3
        for i in range(nrot):
            res = rotate_matrix(res)
        return res
    def __str__(self):
        return self.id + "(" + str(self.orientation) + ")"

def filt(vals, v):
    res = vals.copy()
    del res[v]
    return res

def intersect(big, small):
    res = {}
    for s in small:
        if s in big:
            res[s] = True
    return res

class Board(object):
    def __init__(self, tilestr):
        self.sz = int(math.sqrt(len(tilestr)))
        self.tiles = {}
        self.left = {}
        self.top = {}
        for id in tilestr:
            tile = Tile(id, tilestr[id])
            self.tiles[id] = tile
            for rot in tile.rotations:
                t, l = rot[0], rot[3]
                if l not in self.left:
                    self.left[l] = {}
                self.left[l][id] = True
                if t not in self.top:
                    self.top[t] = {}
                self.top[t][id] = True
        self.m = [ [ None for x in range(self.sz) ] for y in range(self.sz) ]
    def fits(self, r, c, tile):
        if r > 0:
            if self.m[r-1][c].bottom() != tile.top():
                return False
        if c > 0:
            if self.m[r][c-1].right() != tile.left():
                return False
        return True
    def has_left(self, e):
        if e not in self.left:
            return {}
        return self.left[e]
    def has_top(self, e):
        if e not in self.top:
            return {}
        return self.top[e]
    def solveat(self, r, c, avail, depth = 0):
        if c >= self.sz or r >= self.sz:
            return True, avail
        candidates = avail
        if c > 0:
            possible = self.has_left(self.m[r][c-1].right())
            candidates = intersect(candidates, possible)
        if r > 0:
            possible = self.has_top(self.m[r-1][c].bottom())
            candidates = intersect(candidates, possible)
        for tid in candidates:
            tile = copy.copy(self.tiles[tid])
            assert(tile.orientation == 0)
            for i in range(tile.num_orientations()):
                tile.orient(i)
                if not self.fits(r, c, tile):
                    continue
                self.m[r][c] = tile
                ok, avail2 = self.solveat(r, c+1, filt(avail, tid), depth+1)
                if not ok:
                    continue
                if c == 0:
                    ok, avail2 = self.solveat(r+1, c, avail2, depth+1)
                if ok:
                    return ok, avail2
        return False, avail

    def solve(self):
        avail = {}
        for tid in self.tiles:
            avail[tid] = True
        return self.solveat(0, 0, avail)

    def image(self):
        tiles = [ [ None for x in range(self.sz) ] for y in range(self.sz) ]
        for r in range(len(self.m)):
            for c in range(len(self.m[0])):
                tiles[r][c] = self.m[r][c].image()
        h, w = len(tiles)*len(tiles[0][0]), len(tiles[0])*len(tiles[0][0][0])
        img = [ [ None for x in range(w)] for y in range(h) ]
        row = 0
        for r in tiles: # r is a row of tiles
            for i in range(len(r[0])): # i is a line of pixels in a row of tiles
                col = 0
                for tile in r: # t is a tile in the row
                    for c in tile[i]: # c is a character in the ith row of r
                        img[row][col] = c
                        col += 1
                row += 1
        return img

    def corners(self):
        return [ self.m[0][0], self.m[0][-1], self.m[-1][0], self.m[-1][-1] ]

    def boardstr(self):
        res = ""
        for r in self.m:
            res += " ".join([str(x) for x in r]) + "\n"
        return res
    def __str__(self):
        return "\n".join([ str(self.tiles[id])  for id in self.tiles])

def part1(tilestr):
    b = Board(tilestr)
    ok = b.solve()
    if not ok:
        return 0
    print(b.boardstr())
    res = 1
    for tile in b.corners():
        res *= int(tile.id)
    return res

def matrixify(strs):
    m = []
    for s in strs:
        m.append([c for c in s])
    return m

def numhashes(m):
    n = 0
    for r in m:
        for c in r:
            if c == '#':
                n += 1
    return n

def matches(mat,pat,r,c):
    for rr in range(len(pat)):
        for cc in range(len(pat[0])):
            if pat[rr][cc] == '#' and mat[r+rr][c+cc] != '#':
                return False
    return True

def mark(mat,pat,r,c):
    for rr in range(len(pat)):
        for cc in range(len(pat[0])):
            if pat[rr][cc] == '#':
                mat[r+rr][c+cc] = 'O'

def convolve(mat, pat):
    n = 0
    for r in range(0, len(mat)-len(pat)+1):
        for c in range(0, len(mat[0])-len(pat[0])+1):
            if matches(mat,pat,r,c):
                mark(mat,pat,r,c)
                n += 1
    return n>0

def pp(mat):
    for r in mat:
        print(''.join(r))

def part2(tilestr):
    b = Board(tilestr)
    ok = b.solve()
    if not ok:
        return 0
    monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    mm = matrixify(monster)
    m = b.image()
    hm = mhflip(m)
    vm = mvflip(m)
    for i in range(4):
        if convolve(m, mm):
            print("m", i, numhashes(m))
            pp(m)
        if convolve(hm, mm):
            print("hm", i, numhashes(hm))
        if convolve(vm, mm):
            print("vm", i, numhashes(vm))
        m, hm, vm = rotate_matrix(m), rotate_matrix(hm), rotate_matrix(vm)

    return 0

#2414 too high
fn = "input20.txt"
fn = "w"
tilestr = {}
id = 0
with open(fn) as f:
    for l in f:
        l = l.strip()
        if len(l) == 0:
            continue
        m = re.match(r'Tile (\d+):', l)
        if m:
            id = m.group(1)
            tilestr[id] = []
            continue
        if l[0] == '.' or l[0] == '#':
            tilestr[id].append(l)

print(part1(tilestr))
print(part2(tilestr))
