#!/opt/local/bin/python

filename = "input03.txt"
grid = []
with open(filename) as f:
    for l in f:
        grid.append(l.strip())
w = len(grid[0]) # assume all rows have the same width
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
res = []
for ij in slopes:
    pi, pj, i, j, n = ij[0], ij[1], 0, 0, 0
    while j < len(grid):
        if grid[j][i] == '#':
            n += 1
        i = (i + pi) % w
        j = j + pj
    res.append(n)

p = 1
for i in range(len(slopes)):
    print("right", slopes[i][0], "down", slopes[i][1], "->", res[i], "trees")
    p = p * res[i]
print("product =", p)
