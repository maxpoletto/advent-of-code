#!/opt/local/bin/python

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
    p = {}
    for i in n:
        p[i] = 1
    for i in range(len(n)-4, -1, -1):
        p[n[i]] = 0
        for j in range(i+3, i, -1):
            if n[j] - n[i] <= 3:
                p[n[i]] += p[n[j]]
    return p[0]

fn = "input10.txt"
n = []
with open(fn) as f:
    for l in f:
        n.append(int(l))

print(part1(n))
print(part2(n))
