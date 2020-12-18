#!/opt/local/bin/python

import re

tokens = [
    ('num', r'\d+'),
    ('op', r'\+|\*'),
    ('lp', r'\('),
    ('rp', r'\)'),
    ('skip', r'[ \t]+'),
]
regex = re.compile('|'.join('(?P<%s>%s)' % p for p in tokens))

def tokenize(expr):
    for v in regex.finditer(expr):
        kind = v.lastgroup
        val = v.group()
        if kind == 'skip':
            continue
        if kind == 'num':
            val = int(val)
        yield (kind, val)

def eval_op(s):
    while len(s) > 2 and (s[-2] == '+' or s[-2] == '*'):
        v1, op, v2 = s[-3:]
        s = s[:-2]
        if op == '+':
            s[-1] = v1+v2
        elif op == '*':
            s[-1] = v1*v2
    return s

def evaluate1(e):
    """Evaluates parenthesized arithmetic expression e where '+' and '*' have the same precedence."""
    s = []
    for t in tokenize(e):
        kind, val = t
        if kind == 'lp':
            s.append(kind)
        elif kind == 'rp':
            assert(len(s) > 1 and s[-2] == 'lp')
            s[-1] = s.pop()
            s = eval_op(s)
        elif kind == 'op':
            s.append(val)
        elif kind == 'num':
            s.append(val)
            s = eval_op(s)
    return s[0]

def test_evaluate():
    assert evaluate1("2 + 2") == 4
    assert evaluate1("2 * 3 + (4 * 5) ") == 26
    assert evaluate1("5 + (8 * 3 + 9 + 3 * 4 * 3) ") == 437
    assert evaluate1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) ") == 12240
    assert evaluate1("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 ") == 13632

def eval_add(s):
    while len(s) > 2 and s[-2] == '+':
        v = s[-1]
        s = s[:-2]
        s[-1] = s[-1]+v
    return s

def eval_mul(s):
    while len(s) > 2 and s[-2] == '*':
        v = s[-1]
        s = s[:-2]
        s[-1] = s[-1]*v
    if len(s) > 1 and s[-2] == 'lp':
        s[-1] = s.pop()
    return s

def evaluate2(e):
    """Evaluates parenthesized arithmetic expression e where '+' has higher precedence than '*'."""
    s = []
    for t in tokenize(e):
        kind, val = t
        if kind == 'lp':
            s.append(kind)
        elif kind == 'rp':
            s = eval_mul(s)
            s = eval_add(s)
        elif kind == 'op':
            s.append(val)
        elif kind == 'num':
            s.append(val)
            s = eval_add(s)
    s = eval_mul(s)
    return s[0]

def test_evaluate2():
    assert evaluate2("1 + 2 * 3 + 4 * 5 + 6") == 231
    assert evaluate2("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert evaluate2("2 * 3 + (4 * 5)") == 46
    assert evaluate2("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
    assert evaluate2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
    assert evaluate2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340

def part1(m):
    tot = 0
    for e in m:
        tot += evaluate1(e)
    return tot

def part2(m):
    tot = 0
    for e in m:
        tot += evaluate2(e)
    return tot

fn = "input18.txt"
m = []
with open(fn) as f:
    for l in f:
        m.append(l.strip())

test_evaluate()
test_evaluate2()
print(part1(m))
print(part2(m))
