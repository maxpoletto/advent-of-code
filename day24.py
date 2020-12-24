#!/opt/local/bin/python

import copy

def get_dirs(l):
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

class Floor:
    def __init__(self, size):
        h = 2*(size+1)+1
        w = 2*(2*(size+1)+1)
        self.zr = int(h/2)
        self.zc = int(w/2)+self.zr%2-1
        self.grid = [['.' for c in range(w)] for r in range(h)]
        for r in range(h):
            for c in range(r%2, w, 2):
                self.grid[r][c] = 'w'
    def run(self, instrs):
        for dirs in instrs:
            r, c = self.zr, self.zc
            for d in dirs:
                r += d[0]
                c += d[1]
            assert(self.grid[r][c] == 'b' or self.grid[r][c] == 'w')
            if self.grid[r][c] == 'b':
                self.grid[r][c] = 'w'
            elif self.grid[r][c] == 'w':
                self.grid[r][c] = 'b'
    def nn(self, r, c, v):
        n = 0
        for d in [[0,2],[0,-2],[-1,1],[-1,-1],[1,1],[1,-1]]:
            n += (self.grid[r+d[0]][c+d[1]] == v)
        return n
    def update(self):
        g2 = copy.deepcopy(self.grid)
        for r in range(1, len(self.grid)-1):
            for c in range(2, len(self.grid[0])-2):
                v = self.grid[r][c]
                if v == '.':
                    continue
                n = self.nn(r, c, 'b')
                if v == 'b' and (n == 0 or n > 2):
                    g2[r][c] = 'w'
                if v == 'w' and n == 2:
                    g2[r][c] = 'b'
        self.grid = g2
    def count(self, v):
        n = 0
        for r in self.grid:
            for c in r:
                if c == v:
                    n += 1
        return n
    def __str__(self):
        res = "{} {}\n".format(len(self.grid), len(self.grid[0]))
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if r == self.zr and c == self.zc:
                    res += '*'
                else:
                    res += self.grid[r][c]
            res += "\n"
        return res

def part1(instrs):
    maxlen = 0
    for i in instrs:
        maxlen = max(maxlen,len(i))
    f = Floor(maxlen)
    f.run(instrs)
    return f.count('b')

def part2(instrs):
    maxlen = 0
    for i in instrs:
        maxlen = max(maxlen,len(i))
    f = Floor(maxlen)
    f.run(instrs)
    for i in range(100):
        f.update()
        print(i+1, f.count('b'))
    return f.count('b')

fn = "input24.txt"
fn = "w"
with open(fn) as f:
    instrs = []
    for l in f:
        instrs.append(get_dirs(l.strip()))

print(part1(instrs))
print(part2(instrs))
