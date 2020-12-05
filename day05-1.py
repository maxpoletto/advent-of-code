#!/opt/local/bin/python

filename = "input05.txt"
max_id = 0
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
        if r*8+c > max_id:
            max_id = r*8+c
print("max id", max_id)
