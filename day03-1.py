#!/opt/local/bin/python

filename = "input03.txt"
grid = []
with open(filename) as f:
    for l in f:
        grid.append(l.strip())
w = len(grid[0]) # assume all rows have the same width
i, n = 0, 0
for j in range(len(grid)):
    if grid[j][i] == '#':
        n += 1
    i = (i + 3) % w
print("We encountered", n, "trees")
