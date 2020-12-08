#!/opt/local/bin/python

import copy

fn = "input08.txt"
def run(code):
    p, a = 0, 0
    while p >= 0 and p < len(code):
        op, val, vis = code[p]
        if vis == True:
            return (False, 0)
        code[p][2] = True
        if op == "nop":
            p += 1
        elif op == "acc":
            a += val
            p += 1
        elif op == "jmp":
            p += val
    return (p >= len(code), a)

code = []
with open(fn) as f:
    for l in f:
        l = l.strip()
        op, val = l.split(" ")
        code.append([op, int(val), False])

for i in range(len(code)-1, -1, -1):
    if code[i][0] == "acc":
        continue
    c = copy.deepcopy(code)
    if c[i][0] == "nop":
        c[i][0] = "jmp"
    else:
        c[i][0] = "nop"
    ok, acc = run(c)
    if ok:
        print(acc)
        break
