#!/opt/local/bin/python

import copy

class World(object):
    """
    docstring
    """
    def __init__(self, lines, maxturns):
        """
        docstring
        """
        d = max(len(lines), len(lines[0]))
        self.size = d + 2*maxturns
        self.zero = maxturns
        self.dirs = [[x, y, z] for x in [-1,0,1]
            for y in [-1,0,1] for z in [-1,0,1] if x != 0 or y != 0 or z != 0]
        self.m = self.__blank()
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                self.m[self.zero][y+self.zero][x+self.zero] = lines[y][x]

    def __blank(self):
        m = [None]*self.size
        for z in range(self.size):
            m[z] = [None]*self.size
            for y in range(self.size):
                m[z][y] = ['.']*self.size
        return m

    def nn(self, x, y, z, v):
        n = 0
        for d in self.dirs:
            xx, yy, zz = x+d[0], y+d[1], z+d[2]
            if self.m[zz][yy][xx] == v:
                n += 1
        return n
    
    def step(self):
        m2 = self.__blank()
        for z in range(1, self.size-1):
            for y in range(1, self.size-1):
                for x in range(1, self.size-1):
                    if self.m[z][y][x] == '#':
                        n = self.nn(x,y,z,'#')
                        if n == 2 or n == 3:
                            m2[z][y][x] = '#'
                    elif self.m[z][y][x] == '.':
                        n = self.nn(x,y,z,'#')
                        if n == 3:
                            m2[z][y][x] = '#'
        self.m = m2

    def print(self):
        for z in range(self.size):
            print("z=", z-self.zero)
            for y in range(self.size):
                for x in range(self.size):
                    print(self.m[z][y][x], end='')
                print()
        print(self.size, self.zero, self.dirs, len(self.dirs))

    def nactive(self):
        n = 0
        for z in range(1, self.size-1):
            for y in range(1, self.size-1):
                for x in range(1, self.size-1):
                    if self.m[z][y][x] == '#':
                        n+=1
        return n

'''
    def __p2i(p):
        [x, y, z] = p
        return x + self.size * (y + z * self.size)
    def __i2p(i):
        z = int(i / (self.size*self.size))
        r = i % (self.size*self.size)
        y = 
        z = 
'''

class World4(object):
    """
    docstring
    """
    def __init__(self, lines, maxturns):
        """
        docstring
        """
        d = max(len(lines), len(lines[0]))
        self.size = d + 2*maxturns
        self.zero = maxturns
        self.dirs = [[x, y, z, w] for x in [-1,0,1]
            for y in [-1,0,1] for z in [-1,0,1] for w in [-1, 0, 1] if x != 0 or y != 0 or z != 0 or w != 0]
        self.m = self.__blank()
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                self.m[self.zero][self.zero][y+self.zero][x+self.zero] = lines[y][x]

    def __blank(self):
        m = [None]*self.size
        for w in range(self.size):
            m[w] = [None]*self.size
            for z in range(self.size):
                m[w][z] = [None]*self.size
                for y in range(self.size):
                    m[w][z][y] = ['.']*self.size
        return m

    def nn(self, x, y, z, w, v):
        n = 0
        for d in self.dirs:
            xx, yy, zz, ww = x+d[0], y+d[1], z+d[2], w+d[3]
            if self.m[ww][zz][yy][xx] == v:
                n += 1
        return n
    
    def step(self):
        m2 = self.__blank()
        for w in range(1, self.size-1):
            for z in range(1, self.size-1):
                for y in range(1, self.size-1):
                    for x in range(1, self.size-1):
                        if self.m[w][z][y][x] == '#':
                            n = self.nn(x,y,z,w,'#')
                            if n == 2 or n == 3:
                                m2[w][z][y][x] = '#'
                        elif self.m[w][z][y][x] == '.':
                            n = self.nn(x,y,z,w,'#')
                            if n == 3:
                                m2[w][z][y][x] = '#'
        self.m = m2

    def print(self):
        for w in range(self.size):
            for z in range(self.size):
                print("w=", w-self.zero, "z=", z-self.zero)
                for y in range(self.size):
                    for x in range(self.size):
                        print(self.m[w][z][y][x], end='')
                    print()
        print(self.size, self.zero, self.dirs, len(self.dirs))

    def nactive(self):
        n = 0
        for w in range(1, self.size-1):
            for z in range(1, self.size-1):
                for y in range(1, self.size-1):
                    for x in range(1, self.size-1):
                        if self.m[w][z][y][x] == '#':
                            n+=1
        return n

'''
    def __p2i(p):
        [x, y, z] = p
        return x + self.size * (y + z * self.size)
    def __i2p(i):
        z = int(i / (self.size*self.size))
        r = i % (self.size*self.size)
        y = 
        z = 
'''

def part1(w):
    return 0

def part2(m):
    return 0

fn = "input17.txt"
#fn = "t"
m = []
with open(fn) as f:
    for l in f:
        m.append(l.strip())

w = World4(m, 7)
for i in range(6):
    w.step()
    print(i)
print(w.nactive())
