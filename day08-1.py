#!/opt/local/bin/python

fn = "input08.txt"
code = []
with open(fn) as f:
    for l in f:
        l = l.strip()
        op, val = l.split(" ")
        code.append([op, int(val), False])

p, a = 0, 0
while p >= 0 and p < len(code):
    op, val, vis = code[p]
    if vis == True:
        print(a)
        break
    code[p][2] = True
    if op == "nop":
        p += 1
    elif op == "acc":
        a += val
        p += 1
    elif op == "jmp":
        p += val
