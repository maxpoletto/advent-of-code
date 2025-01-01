from math import gcd

def read_input():
    m = []
    with open("input/i08.txt") as f:
        for l in f:
            m.append(list(l.strip()))
    antennas = {}
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] != '.':
                antennas.setdefault(m[r][c], []).append((r, c))
    return m, antennas

def inbounds(m, n):
    return 0 <= n[0] < len(m) and 0 <= n[1] < len(m[0])

def find_antinodes_pair(m, a1, a2):
    r1, c1 = a1
    r2, c2 = a2
    dr, dc = r2 - r1, c2 - c1
    for n in [(r1 - dr, c1 - dc), (r2 + dr, c2 + dc)]:
        if inbounds(m, n):
            yield n

def find_antinodes_inline(m, a1, a2):
    if a1[0] == a2[0]: # Same row
        for c in range(0, len(m[0])):
            yield(a1[0], c) 
    elif a1[1] == a2[1]: # Same column
        for r in range(0, len(m)):
            yield(r, a1[1])
    else:
        dr, dc = a2[0] - a1[0], a2[1] - a1[1]
        g = gcd(dr, dc)
        dr, dc = dr // g, dc // g
        xr, xc = 0, 0
        while inbounds(m, (a1[0] + xr, a1[1] + xc)):
            yield (a1[0] + xr, a1[1] + xc)
            xr += dr
            xc += dc
        xr, xc = -dr, -dc
        while inbounds(m, (a1[0] + xr, a1[1] + xc)):
            yield (a1[0] + xr, a1[1] + xc)
            xr -= dr
            xc -= dc

def count_antinodes(finder):
    m, antennas = read_input()
    antinodes = set()
    for a, coords in antennas.items():
        # Find all pairs of coordinates
        for c1 in coords:
            for c2 in coords:
                if c1 == c2:
                    continue
                for n in finder(m, c1, c2):
                    antinodes.add(n)
    print(len(antinodes))

# Part 1
count_antinodes(find_antinodes_pair)

# Part 2
count_antinodes(find_antinodes_inline)
