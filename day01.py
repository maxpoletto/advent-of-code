#!/opt/local/bin/python

def part1(n, target):
    i, j = 0, len(n)-1
    while i < j:
        s = n[i]+n[j]
        if s > target:
            j = j-1
        elif s < target:
            i = i+1
        else:
            return n[i]*n[j]
    return -1

def part2(n, target):
    for k in range(len(n)-2):
        t = target-n[k]
        i, j = k+1, len(n)-1
        while i < j:
            s = n[i]+n[j]
            if s > t:
                j = j-1
            elif s < t:
                i = i+1
            else:
                return n[i]*n[j]*n[k]
    return -1

filename = "input01.txt"
n = []
with open(filename) as f:
    for l in f:
        n.append(int(l))
n.sort()
print(part1(n, 2020))
print(part2(n, 2020))
