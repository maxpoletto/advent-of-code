#!/usr/local/bin/python
 
def val_at_pos(rr, cc):
    r, c, n = 1, 1, 20151125
    while r < rr or c < cc:
        n = (n * 252533) % 33554393
        r, c = r-1, c+1
        if r == 0:
            r, c = c, 1
    return n

print(val_at_pos(2978, 3083))
