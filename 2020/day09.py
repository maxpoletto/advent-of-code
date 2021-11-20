#!/usr/local/bin/python

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

def adds_up_to(d, n):
    for m in d:
        if n-m in d:
            return True
    return False

def solve(v, k):
    """Finds the first number in n that is not the sum of the k previous
    numbers in n. Complexity is O(k*|v|).
    """
    d = {}
    for i in range(0, k):
        add(d, v[i])
    for i in range(k, len(v)):
        if not adds_up_to(d, v[i]):
            return v[i]
        sub(d, v[i-k])
        add(d, v[i])

def part1(n):
    return solve(n, 25)

def part2(n):
    target = solve(n, 25)
    i, j = 0, 1
    sum = n[i]+n[j]
    while True:
        if sum == target:
            n2 = sorted(n[i:j+1])
            return n2[0]+n2[-1]
        elif sum > target:
            sum -= n[i]
            i += 1
            if i < j:
                continue
            j += 1
        else:
            j += 1
        if j > len(n):
            break
        sum += n[j]
    return -1

fn = "input09.txt"
n = []
with open(fn) as f:
    for l in f:
        n.append(int(l))

print(part1(n))
print(part2(n))
