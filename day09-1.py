#!/opt/local/bin/python

import time

# Simple O(n*k*log(k)) version (where k is the length of the preamble)

def adds_up_to(n, target):
    n = sorted(n)
    i, j = 0, len(n)-1
    while i < j:
        s = n[i]+n[j]
        if s > target:
            j = j-1
        elif s < target:
            i = i+1
        else:
            return True
    return False

def solve(n, pre):
    for i in range(pre, len(n)):
        if not adds_up_to(n[i-pre:i],n[i]):
            return(n[i])
    return -1

# More involved but much faster O(n*k) version.

def add(d, n):
    if n not in d:
        d[n] = 1
    else:
        d[n] += 1

def sub(d, n):
    if d[n] == 1:
        del d[n]
    else:
        d[n] -= 1

def adds_up_to2(d, n):
    for m in d:
        if n-m in d:
            return True
    return False

def solve2(n, pre):
    d = {}
    for i in range(0, pre):
        add(d, n[i])
    for i in range(pre, len(n)):
        if not adds_up_to2(d, n[i]):
            return n[i]
        sub(d, n[i-pre])
        add(d, n[i])

# Main.

def measure(f):
    t = time.perf_counter_ns()
    for _ in range(100):
        f(n, 25)
    return(time.perf_counter_ns()-t)

fn = "input09.txt"
n = []
with open(fn) as f:
    for l in f:
        n.append(int(l))

d1=measure(solve)
d2=measure(solve2)
print(d1, d2, (d2-d1)/d1 * 100, sep="\n")
print(solve(n, 25))
