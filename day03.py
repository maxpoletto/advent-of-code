#!/opt/local/bin/python

def part1(grid):
    i, n = 0, 0
    for j in range(len(grid)):
        if grid[j][i] == '#':
            n += 1
        i = (i + 3) % len(grid[0])
    return n

def part2(grid):
    res = 1
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    for ij in slopes:
        pi, pj, i, j, n = ij[0], ij[1], 0, 0, 0
        while j < len(grid):
            if grid[j][i] == '#':
                n += 1
            i = (i + pi) % len(grid[0])
            j = j + pj
        res *= n
    return res

fn = "input03.txt"
grid = []
with open(fn) as f:
    for l in f:
        grid.append(l.strip())

print(part1(grid))
print(part2(grid))
