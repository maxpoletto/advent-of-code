#!/opt/local/bin/python

filename = "input06.txt"

def count(d, n):
    t = 0
    for i in d:
        if d[i] == n:
            t += 1
    return t

s = 0
d, n = {}, 0
with open(filename) as f:
    for l in f:
        l = l.strip()
        if len(l) == 0:
            s += count(d, n)
            d, n = {}, 0
        else:
            n += 1
            for c in l:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
if n > 0:
    s += count(d, n)
print(s)
