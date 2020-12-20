#!/opt/local/bin/python

import copy
import re
import math

def vert_edge(tile, n):
    return ''.join([ row[n] for row in tile])

def flip(s):
    s2 = ""
    for c in s:
        s2 = c+s2
    return s2

def rotations(v):
    rots = [v]
    for _ in range(0, 3):
        v = v[1:] + v[:1]
        v = [ v[0], flip(v[1]), v[2], flip(v[3])]
        rots.append(v)
    return rots

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
        rot += rotations([ft,l,fb,r]) # flipped horizontally
        rot += rotations([b,fr,t,fl]) # flipped vertically
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
    def line(self, i):
        o = self.orientation
        if o == 0:
            return self.l[i]
        elif o == 1:
            return vert_edge(self.l, len(self.l)-1-i)
        elif o == 2:
            return flip(self.l[len(self.l)-1-i])
        elif o == 3:
            return flip(vert_edge(self.l, i))
        elif o == 4:
            return flip(self.l[i])
        elif o == 5:
            return self.l[len(self.l)-1-i]
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

    def corners(self):
        return [ self.m[0][0], self.m[0][-1], self.m[-1][0], self.m[-1][-1] ]

    def boardstr(self):
        res = ""
        for r in self.m:
            res += " ".join([str(x) for x in r]) + "\n"
        return res

    def vboardstr(self):
        res = ""
        l = self.m[0][0].num_lines()
        for r in self.m:
            for i in range(l):
                res += " ".join([e.line(i) for e in r ]) + "\n"
            res += "\n"
        return res

    def __str__(self):
        return "\n".join([ str(self.tiles[id])  for id in self.tiles])


def part1(tilestr):
    b = Board(tilestr)
    ok = b.solve()
    if not ok:
        return 0
    print(b.vboardstr())
    print(b.boardstr())
    res = 1
    for tile in b.corners():
        res *= int(tile.id)
    return res

def part2(rules, messages):
    b = Board(tilestr)
    ok = b.solve()
    if not ok:
        return 0
    return 0

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
