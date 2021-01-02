#!/opt/local/bin/python

from lib import aodfile, util
import ctypes
import re

class Circuit(object):
    def __init__(self, spec):
        self.v, self.a = {}, {}
        for s in spec:
            [l, r] = s.split(' -> ')
            op = re.findall(r'[A-Z]+', l)
            if len(op) == 0:
                op = ['SET']
            arg = [util.intorstr(x) for x in re.findall(r'(?:[a-z]+|[0-9]+)', l)]
            assert(r not in self.v)
            self.v[r] = [ op[0], arg ]
    def eval(self, v) -> int:
        if type(v) == int:
            return v
        assert(v in self.v)
        if v in self.a:
            return self.a[v]
        [op, arg] = self.v[v]
        if op == 'SET':
            self.a[v] = self.eval(arg[0])
        elif op == 'AND':
            self.a[v] =self.eval(arg[0]) & self.eval(arg[1])
        elif op == 'OR':
            self.a[v] = self.eval(arg[0]) | self.eval(arg[1])
        elif op == 'NOT':
            self.a[v] = ~self.eval(arg[0])
        elif op == 'LSHIFT':
            self.a[v] = self.eval(arg[0]) << self.eval(arg[1])
        elif op == 'RSHIFT':
            self.a[v] = self.eval(arg[0]) >> self.eval(arg[1])
        return self.a[v]

def part1(lines):
    c = Circuit(lines)
    return c.eval('a')

def part2(lines):
    c = Circuit(lines)
    c.v['b'] = ['SET', [956]]
    return c.eval('a')

fn = "input/input07.txt"
lines = aodfile.stripped_lines(fn)
print(part1(lines))
print(part2(lines))
