from collections import deque
from operator import xor, and_, or_
_funcs = { 'XOR': xor, 'AND': and_, 'OR': or_ }
class Adder:
    def __init__(self, s):
        lines = s.split('\n')
        self.gates, self.values = {}, {}
        for l in lines:
            if ':' in l:
                n, v = l.strip().split(': ')
                self.values[n] = int(v)
            elif '-' in l:
                x = l.strip().split(' ')
                in1, func, in2, out = x[0], x[1], x[2], x[4]
                self.gates.setdefault(in1, []).append((in2, out, func))
                self.gates.setdefault(in2, []).append((in1, out, func))
    def calc(self):
        q = deque(self.values)
        while q:
            in1 = q.popleft()
            for in2, out, func in self.gates.get(in1, []):
                if in2 in self.values and out not in self.values:
                    self.values[out] = _funcs[func](self.values[in1], self.values[in2])
                    q.append(out)
        zs = sorted([k for k in self.values if k[0] == 'z'])
        return sum(1 << i for i, z in enumerate(zs) if self.values[z])

def part1():
    with open('input/i24.txt') as f:
        adder = Adder(f.read())
        print(adder.calc())

part1()
