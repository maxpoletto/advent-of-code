#!/opt/local/bin/python

def to_binary(s, zero):
    r = 0
    for x in s:
        if x == zero:
            r <<= 1
        else:
            r = (r<<1) | 0x1
    return r

def seat_ids(seats):
    ids = []
    for s in seats:
        r = to_binary(s[:7], 'F')
        c = to_binary(s[7:], 'L')
        ids.append(r*8+c)
    return ids

def part1(seats):
    return max(seat_ids(seats))

def part2(seats):
    s = sorted(seat_ids(seats))
    for i in range(1, len(s)):
        if s[i] - s[i-1] == 2:
            return s[i]-1

fn = "input05.txt"
seats = []
with open(fn) as f:
    for l in f:
        seats.append(l.strip())

print(part1(seats))
print(part2(seats))
