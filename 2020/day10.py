#!/usr/local/bin/python

def part1(n):
    n = [0] + sorted(n)
    d1, d3 = 0, 1
    for i in range(0, len(n)-1):
        if n[i+1] - n[i] == 1:
            d1 += 1
        elif n[i+1] - n[i] == 3:
            d3 += 1
    return d1*d3

def part2(n):
    n = [0] + sorted(n)
    n.append(n[-1]+3) # Append final element as sentinel.
    p = [0] * (len(n)-3) + [1, 1, 1]
    # p[i] = number of paths starting at n[i].
    # By definition, only 1 path to the last element from each of the last 3.
    for i in range(len(n)-4, -1, -1):
        for j in range(i+3, i, -1):
            if n[j] - n[i] <= 3:
                p[i] += p[j]
    return p[0]

fn = "input10.txt"
n = []
with open(fn) as f:
    for l in f:
        n.append(int(l))

print(part1(n))
print(part2(n))
