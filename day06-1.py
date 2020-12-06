#!/opt/local/bin/python

filename = "input06.txt"

s = 0
d = {}
with open(filename) as f:
    for l in f:
        l = l.strip()
        if len(l) == 0:
            s += len(d)
            d = {}
        else:
            for c in l:
                d[c] = True
if len(d) > 0:
    s += len(d)
print(s)
