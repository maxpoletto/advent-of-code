#!/opt/local/bin/python

class World():
    def __init__(self, lines, ndims, maxturns):
        assert len(lines) == len(lines[0])
        self.dim = len(lines)+2*maxturns
        self.zero = maxturns
        self.ndims = ndims
        self.noff = [0] * 3**ndims
        l = 1
        for i in range(ndims):
            m = self.dim**i
            for j in range(l):
                self.noff[l+j] = self.noff[j] + m
                self.noff[2*l+j] = self.noff[j] - m
            l *= 3
        self.noff = sorted(self.noff[1:])
        self.curbuf = 0
        sz = self.dim**self.ndims + 2*max(self.noff)
        self.min = max(self.noff)
        self.max = sz - max(self.noff)
        self.buf = [ [False]*sz, [False]*sz ]
        for y in range(len(lines)):
            for x in range(len(lines)):
                if lines[y][x] == '#':
                    self.set_pt([x, y])
    def set_pt(self, p):
        assert(self.ndims >= len(p))
        i, m, pos = 0, 1, 0
        while i < len(p):
            pos += (self.zero+p[i])*m
            m *= self.dim
            i += 1
        while i < self.ndims:
            pos += self.zero*m
            m *= self.dim
            i += 1
        self.buf[self.curbuf][self.min+pos] = True
    def step(self, steps):
        for _ in range(steps):
            buf0 = self.buf[self.curbuf]
            buf1 = self.buf[1-self.curbuf]
            for i in range(self.min, self.max):
                n = 0
                for j in self.noff:
                    n += buf0[i+j]
                buf1[i] = n == 3 or (n == 2 and buf0[i])
            self.curbuf = 1-self.curbuf
    def nactive(self):
        return self.buf[self.curbuf].count(True)

def test():
    m = [
        '.#.',
        '..#',
        '###',
    ]
    w = World(m, 3, 6)
    w.step(6)
    assert(w.nactive() == 112)
    w = World(m, 4, 6)
    w.step(6)
    assert(w.nactive() == 848)

def part1(m):
    w = World(m, 3, 6)
    w.step(6)
    return w.nactive()
def part2(m):
    w = World(m, 4, 6)
    w.step(6)
    return w.nactive()

fn = "input17.txt"
m = []
with open(fn) as f:
    for l in f:
        m.append(l.strip())
#test()
#print(part1(m))
print(part2(m))
