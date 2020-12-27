#!/opt/local/bin/python

from lib import mat
import copy
import math
import re

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

class Tile(object):
    """Represents a single tile, which can be flipped and rotated."""
    def __init__(self, id, lines):
        self.id = id
        m = mat.matrixify(lines)
        assert(len(m) == len(m[0]))
        self.m = []
        for _ in range(4):
            self.m.append(m)
            m = mat.rotate(m)
        m = mat.flip(m)
        for _ in range(4):
            self.m.append(m)
            m = mat.rotate(m)
        r = []
        for m in self.m:
            r.append([mat.row(m, 0), mat.col(m, len(m)-1), mat.row(m, len(m)-1), mat.col(m, 0)])
        self.rotations = r
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
    def image(self):
        m = self.m[self.orientation]
        res = []
        for i in range(1, len(m)-1):
            res.append([ c for c in m[i][1:-1]])
        return res
    def __str__(self):
        return self.id + "(" + str(self.orientation) + ")"

class Board(object):
    """Represents a board, which is a square grid of tiles."""
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
    def __fits(self, r, c, tile):
        if r > 0:
            if self.m[r-1][c].bottom() != tile.top():
                return False
        if c > 0:
            if self.m[r][c-1].right() != tile.left():
                return False
        return True
    def __has_left(self, e):
        if e not in self.left:
            return {}
        return self.left[e]
    def __has_top(self, e):
        if e not in self.top:
            return {}
        return self.top[e]
    def __solveat(self, r, c, avail):
        if c >= self.sz or r >= self.sz:
            return True, avail
        # Constrain the search.
        candidates = avail
        if c > 0:
            possible = self.__has_left(self.m[r][c-1].right())
            candidates = intersect(candidates, possible)
        if r > 0:
            possible = self.__has_top(self.m[r-1][c].bottom())
            candidates = intersect(candidates, possible)
        # Try all remaining candidates at (r,c).
        for tid in candidates:
            tile = copy.copy(self.tiles[tid])
            assert(tile.orientation == 0)
            for i in range(tile.num_orientations()):
                tile.orient(i)
                if not self.__fits(r, c, tile):
                    continue
                self.m[r][c] = tile
                # Recurse right...
                ok, avail2 = self.__solveat(r, c+1, filt(avail, tid))
                if not ok:
                    continue
                if c == 0:
                    # ... and then recurse down.
                    ok, avail2 = self.__solveat(r+1, c, avail2)
                if ok:
                    return ok, avail2
        return False, avail
    def solve(self):
        """Tries to arranges the board so that tile edges align, and returns
        True/False on success/failure.
        """
        avail = {}
        for tid in self.tiles:
            avail[tid] = True
        return self.__solveat(0, 0, avail)[0]
    def image(self):
        """Returns a "pixel" matrix based on the current tile configuration,
        with tile borders elided.
        """
        tiles = [ [ None for x in range(self.sz) ] for y in range(self.sz) ]
        for r in range(len(self.m)):
            for c in range(len(self.m[0])):
                tiles[r][c] = self.m[r][c].image()
        h, w = len(tiles)*len(tiles[0][0]), len(tiles[0])*len(tiles[0][0][0])
        img = [ [ None for x in range(w)] for y in range(h) ]
        rr = 0
        for r in tiles: # r is a row of tiles
            for i in range(len(r[0])): # i is a line of pixels in a row of tiles
                cc = 0
                for tile in r: # t is a tile in the row
                    for c in tile[i]: # c is a character in the ith row of r
                        img[rr][cc] = c
                        cc += 1
                rr += 1
        return img
    def corners(self):
        return [ self.m[0][0], self.m[0][-1], self.m[-1][0], self.m[-1][-1] ]
    def __str__(self):
        return "\n".join([ " ".join([ str(tile) for tile in r]) for r in self.m])

"""
Helpers for part 2.
"""

def numhashes(m):
    n = 0
    for r in m:
        n += r.count('#')
    return n

def matches(mat, pat, r, c):
    """Returns whether pat matches mat starting at top left corner (r,c) in mat."""
    for rr in range(len(pat)):
        for cc in range(len(pat[0])):
            if pat[rr][cc] == '#' and mat[r+rr][c+cc] != '#':
                return False
    return True

def mark(mat, pat, r, c):
    """Overwrites mat with the pattern given by pat starting at (r,c)."""
    for rr in range(len(pat)):
        for cc in range(len(pat[0])):
            if pat[rr][cc] == '#':
                mat[r+rr][c+cc] = 'O'

def convolve(mat, pat):
    """Finds all matches of pat over mat, where mat and pat are both 2D matrices
    and pat is no bigger than mat along both axes."""
    assert(len(mat) >= len(pat) and len(mat[0]) >= len(pat[0]))
    n = 0
    for r in range(0, len(mat)-len(pat)+1):
        for c in range(0, len(mat[0])-len(pat[0])+1):
            if matches(mat, pat, r, c):
                mark(mat, pat, r, c)
                n += 1
    return n > 0

"""
Main.
"""

def part1(tilestr):
    b = Board(tilestr)
    ok = b.solve()
    print(b)
    if not ok:
        return 0
    res = 1
    for tile in b.corners():
        res *= int(tile.id)
    return res

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
    m = mat.matrixify(monster)
    im = b.image()
    fm = mat.flip(im)
    for _ in range(4):
        if convolve(im, m):
            return numhashes(im)
        if convolve(fm, m):
            return numhashes(fm)
        im, fm = mat.rotate(im), mat.rotate(fm)
    return 0

fn = "input20.txt"
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
