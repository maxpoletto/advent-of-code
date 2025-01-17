from collections import deque
from operator import xor, and_, or_
import sys
_funcs = { 'XOR': xor, 'AND': and_, 'OR': or_ }
def _canonical(a, b):
    return (a, b) if a < b else (b, a)
class Adder:
    def __init__(self, s):
        lines = s.split('\n')
        self.out, self.fwd, self.rev, self.inputs = {}, {}, {}, {}
        self.swaps = []
        for l in lines:
            if ':' in l:
                n, v = l.strip().split(': ')
                self.inputs[n] = int(v)
            elif '-' in l:
                x = l.strip().split(' ')
                in1, func, in2, out = x[0], x[1], x[2], x[4]
                self.out.setdefault(in1, []).append(out)
                self.out.setdefault(in2, []).append(out)
                in1, in2 = _canonical(in1, in2)
                self.fwd[(in1, in2, func)] = out
                if out not in self.rev:
                    self.rev[out] = (in1, in2, func)
    def dot(self):
        l = ["digraph G {"]
        for k, v in self.inputs.items():
            l.append(f'{k} [label = "{k} = {v}"]')
        for i, k in enumerate(self.rev):
            in1, in2, func = self.rev[k]
            l.append(f'func{i} [label = "{func}"]')
            l.append(f'{in1} -> func{i}')
            l.append(f'{in2} -> func{i}')
            l.append(f'func{i} -> {k}')
        l.append('}')
        return '\n'.join(l)
    def swap(self, out1, out2):
        # Does not swap self.out (only necessary if we wanted to compute after the fix.)
        self.rev[out1], self.rev[out2] = self.rev[out2], self.rev[out1]
        self.fwd[self.rev[out1]], self.fwd[self.rev[out2]] = self.fwd[self.rev[out2]], self.fwd[self.rev[out1]]
        self.swaps.append((out1, out2))
    def calc(self):
        values = self.inputs.copy()
        q = deque(values)
        while q:
            n = q.popleft()
            for out in self.out.get(n, []):
                if out in values:
                    continue
                in1, in2, func = self.rev[out]
                if in1 in values and in2 in values:
                    values[out] = _funcs[func](values[in1], values[in2])
                    q.append(out)
        zs = sorted([k for k in values if k[0] == 'z'])
        return sum(1 << i for i, z in enumerate(zs) if values[z])
    def fix(self):
        # Reference:
        # https://en.wikipedia.org/wiki/Adder_(electronics)#/media/File:Full-adder_logic_diagram.svg
        def succ(x, y, func):
            t = (*_canonical(x, y), func)
            return self.fwd[t] if t in self.fwd else None
        carry = ""
        bit, maxbit = 0, sum(1 for k in self.rev if k[0] == 'z') - 1
        while bit < maxbit:
            x, y, z = f'x{bit:02d}', f'y{bit:02d}', f'z{bit:02d}'
            x_xor_y, x_and_y = succ(x, y, 'XOR'), succ(x, y, 'AND')
            if bit == 0:
                carry = x_and_y
                bit += 1
                continue
            carry_xor_xxy = succ(carry, x_xor_y, 'XOR')
            if carry_xor_xxy is None:
                self.swap(x_xor_y, x_and_y)
                continue
            if carry_xor_xxy != z:
                self.swap(carry_xor_xxy, z)
                continue
            # At this point, x_xor_y is correct.
            carry_and_xxy = succ(carry, x_xor_y, 'AND')
            carry = succ(carry_and_xxy, x_and_y, 'OR')
            bit += 1
        return self.swaps

def main():
    f = open('input/i24.txt')
    adder = Adder(f.read())
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case "print": print(adder.dot())
            case "printfixed":
                adder.fix()
                print(adder.dot())
    else:
        print(adder.calc())
        swaps = adder.fix()
        print(f'Pairwise swaps: {swaps}')
        print(','.join(sorted([x for swap in swaps for x in swap])))

main()
