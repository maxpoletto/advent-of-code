#!/opt/local/bin/python

filename = "input01.txt"
target = 2020

n = []
with open(filename) as f:
    for l in f:
        n.append(int(l))
n.sort()
print(len(n))
for k in range(len(n)-2):
    if n[k] >= target:
        break
    t = target-n[k]
    i, j = k+1, len(n)-1
    while True:
        if i >= j:
            break
        s = n[i]+n[j]
        if s > t:
            j = j-1
        elif s < t:
            i = i+1
        else:
            print(", ".join([str(x) for x in sorted([n[i], n[j], n[k]])]), "add up to", target, "and their product is", n[i]*n[j]*n[k])
            exit(0)
print("Not found")
