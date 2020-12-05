#!/opt/local/bin/python

filename = "input05.txt"
ids = []
with open(filename) as f:
    for l in f:
        l = l.strip()
        r, c = 0, 0
        for x in l[:7]:
            if x == 'F':
                r *= 2
            else:
                r = (r<<1) | 0x1
        for x in l[7:]:
            if x == 'L':
                c = (c<<1)
            else:
                c = (c<<1) | 0x1
        ids.append(r*8+c)

s = sorted(ids)
for i in range(1,len(s)):
    if s[i] - s[i-1] == 2:
        print("available seat with id", s[i]-1)
