import re

v = False

def read_input():
    eqs = []
    with open("input/i07.txt") as f:
        for l in f:
            eqs.append(list(map(int, re.split(r'[:\s]+', l.strip()))))
    return eqs

def calc(want, cur, rest, text):
    if len(rest) == 0:
        if cur == want and v:
            print(want, text)
        return cur == want
    if cur > want:
        return False
    return (calc(want, cur + rest[0], rest[1:], text + f"+{rest[0]}") or
            calc(want, cur * rest[0], rest[1:], text + f"*{rest[0]}"))

def calc2(want, cur, rest, text):
    if len(rest) == 0:
        if cur == want and v:
            print(want, text)
        return cur == want
    if cur > want:
        return False
    return (calc2(want, cur + rest[0], rest[1:], text + f"+{rest[0]}") or
            calc2(want, cur * rest[0], rest[1:], text + f"*{rest[0]}") or
            calc2(want, int(str(cur) + str(rest[0])), rest[1:], text + f"||{rest[0]}"))

def solve(func):
    eqs = read_input()
    tot = 0
    for eq in eqs:        
        res = eq[0]
        if func(res, eq[1], eq[2:], f"{eq[1]}"):
            tot += res
    print(tot)

solve(calc)
solve(calc2)
