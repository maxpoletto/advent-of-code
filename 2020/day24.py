#!/usr/local/bin/python

import copy

class Floor:
    W, B, X = 0, 1, 2
    def __init__(self, size):
        """Creates a new tiled floor with at least size tiles in every direction
        from the center."""
        h = 2*(size+1)+1
        w = 2*h
        self.zr = int(h/2)
        self.zc = int(w/2)+self.zr%2-1
        self.grid = [[self.X for c in range(w)] for r in range(h)]
        for r in range(h):
            for c in range(r%2, w, 2):
                self.grid[r][c] = self.W
    def flip_tiles(self, instrs):
        """For each list of directions in instrs, flips the tile reached by
        following those directions starting at the center tile.
        """
        for dirs in instrs:
            r, c = self.zr, self.zc
            for d in dirs:
                r += d[0]
                c += d[1]
            assert(self.grid[r][c] != self.X)
            self.grid[r][c] = 1 - self.grid[r][c]
    def nn(self, r, c, v):
        """Returns number of neighbors of (r,c) that have value v."""
        n = 0
        for d in [[0,2],[0,-2],[-1,1],[-1,-1],[1,1],[1,-1]]:
            n += (self.grid[r+d[0]][c+d[1]] == v)
        return n
    def update(self):
        """Flips every tile that has a certain combination of neighbors."""
        g2 = copy.deepcopy(self.grid)
        for r in range(1, len(self.grid)-1):
            for c in range(2+r%2, len(self.grid[0])-2, 2):
                v = self.grid[r][c]
                assert(v != self.X)
                n = self.nn(r, c, self.B)
                if (v == self.B and (n == 0 or n > 2)) or (v == self.W and n == 2):
                    g2[r][c] = 1 - g2[r][c]
        self.grid = g2
    def count(self, v):
        """Returns the number of tiles of color v."""
        n = 0
        for r in self.grid:
            n += r.count(v)
        return n
    def __str__(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                x = ['w','b','.'][self.grid[r][c]]
                if r == self.zr and c == self.zc:
                    x = x.upper()
                res += x
            res += "\n"
        return res
    @classmethod
    def parse_dirs(_, l):
        d = []
        while len(l) > 0:
            if l[:1] == "e":
                d.append([0,2])
                l = l[1:]
            elif l[:1] == "w":
                d.append([0,-2])
                l = l[1:]
            elif l[:2] == "ne":
                d.append([-1,1])
                l = l[2:]
            elif l[:2] == "nw":
                d.append([-1,-1])
                l = l[2:]
            elif l[:2] == "se":
                d.append([1,1])
                l = l[2:]
            elif l[:2] == "sw":
                d.append([1,-1])
                l = l[2:]
        return d

def part1(instrs, maxlen):
    f = Floor(maxlen)
    f.flip_tiles(instrs)
    return f.count(Floor.B)

def part2(instrs, maxlen):
    f = Floor(maxlen+100)
    f.flip_tiles(instrs)
    for _ in range(100):
        f.update()
    return f.count(Floor.B)

fn = "input24.txt"
with open(fn) as f:
    instrs, maxlen = [], 0
    for l in f:
        instrs.append(Floor.parse_dirs(l.strip()))
        maxlen = max(maxlen, len(instrs[-1]))

print(part1(instrs, maxlen))
print(part2(instrs, maxlen))
