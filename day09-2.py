#!/opt/local/bin/python

import time

# From part 1.
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

# Quadratic.
def weakness1(n, target):
    for i in range(0, len(n)-1):
        sum = n[i]
        for j in range(i+1, len(n)):
            sum += n[j]
            if sum == target:
                n2 = sorted(n[i:j+1])
                return n2[0]+n2[-1]
            elif sum > target:
                break
    return -1

# Linear (~100x faster on given input).
def weakness2(n, target):
    i, j = 0, 1
    sum = n[i]+n[j]
    while True:
        if sum == target:
            n2 = sorted(n[i:j+1])
            return n2[0]+n2[-1]
        elif sum > target:
            sum -= n[i]
            i += 1
            if i < j: continue
            j += 1
        else:
            j += 1
        if j > len(n): break
        sum += n[j]
    return -1

# Main.

def measure(f, target):
    t = time.perf_counter_ns()
    for _ in range(100):
        f(n, target)
    return(time.perf_counter_ns()-t)

fn = "input09.txt"
n = []
with open(fn) as f:
    for l in f:
        n.append(int(l))

target = solve(n, 25)
d1=measure(weakness1, target)
d2=measure(weakness2, target)
print(d1, d2, (d2-d1)/d1 * 100, sep="\n")
print(weakness2(n, target))
