#!/usr/local/bin/python

def run(code):
    p, a = 0, 0
    vis = [False]*len(code)
    while p >= 0 and p < len(code):
        op, val = code[p]
        if vis[p] == True:
            return (False, a)
        vis[p] = True
        if op == "nop":
            p += 1
        elif op == "acc":
            a += val
            p += 1
        elif op == "jmp":
            p += val
    return (p >= len(code), a)

def part1(code):
    return run(code)[1]

def part2(code):
    for i in range(len(code)-1, -1, -1):
        old = code[i][0]
        if old == "nop":
            code[i][0] = "jmp"
        elif old == "jmp":
            code[i][0] = "nop"
        else:
            continue
        ok, acc = run(code)
        if ok:
            return acc
        code[i][0] = old

fn = "input08.txt"
code = []
with open(fn) as f:
    for l in f:
        l = l.strip()
        op, val = l.split(" ")
        code.append([op, int(val)])

print(part1(code))
print(part2(code))
