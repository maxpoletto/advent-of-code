from operator import xor, and_, or_
from pprint import pprint

_funcs = { 'XOR': xor, 'AND': and_, 'OR': or_ }
_gates = {}
class Gate:
    def __init__(self, a, b = None, op = None):
        self.a, self.b, self.op = a, b, op
    def eval(self):
        if self.op is None:
            return self.a
        return _funcs[self.op](_gates[self.a].eval(), _gates[self.b].eval())

def read_input():
    global _gates
    with open('input/i24.txt') as f:
        for l in f:
            if ':' in l:
                n, v = l.strip().split(': ')
                _gates[n] = Gate(int(v))
            elif '-' in l:
                x = l.strip().split(' ')
                in1, in2, func, out = x[0], x[2], x[1], x[4]
                _gates[out] = Gate(in1, in2, func)

def part1():
    zs = sorted([ g for g in _gates if g[0] == 'z'], reverse=True)
    v = 0
    for z in zs:
        v <<= 1
        v |= _gates[z].eval()
    print(v)

read_input()
part1()
