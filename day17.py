#!/opt/local/bin/python

class World(object):
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
        self.noff = self.noff[1:]
        self.buf = [0] * (self.dim**self.ndims)
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
        assert(pos < len(self.buf))
        self.buf[pos] = 1
    def nn(self, i):
        n = 0
        for j in self.noff:
            if i+j >= 0 and i+j < len(self.buf) and self.buf[j+i] == 1:
                n += 1
        return n
    def step(self, steps):
        for _ in range(steps):
            buf = [0] * (self.dim**self.ndims)
            for i in range(len(self.buf)):
                n = self.nn(i)
                buf[i] = int((self.buf[i] == 1 and (n == 2 or n == 3)) or
                    (self.buf[i] == 0 and n == 3))
            self.buf = buf
    def nactive(self):
        return self.buf.count(1)

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
test()
print(part1(m))
print(part2(m))
