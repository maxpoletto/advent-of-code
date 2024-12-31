def part1():
    m = []
    search = 'XMAS';
    lsearch = len(search)
    with open("input/i04.txt") as f:
        for l in f:
            m.append(l.strip())
    w = len(m[0])
    hpad = '.' * (lsearch - 1)
    vpad = hpad + '.' * w + hpad
    m = [ vpad ] * (lsearch - 1) + [ hpad + l + hpad for l in m ] + [ vpad ] * (lsearch - 1)
    hh, ww = len(m), len(m[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1) , (-1, 1)]
    n = 0
    for row in range(lsearch - 1, hh - lsearch + 1):
        for col in range(lsearch - 1, ww - lsearch + 1):
            if m[row][col] != search[0]:
                continue
            for d in dirs:
                r, c = row, col
                for s in search[1:]:
                    r += d[0]
                    c += d[1]
                    if m[r][c] != s:
                        break
                else:
                    n += 1        
    print(n)

def part2():
    m = []
    search = 'MAS'
    with open("input/i04.txt") as f:
        for l in f:
            m.append(l.strip())
    hh, ww = len(m), len(m[0])
    dirs = [(1, 1), (-1, -1), (1, -1) , (-1, 1)]
    n = 0
    for row in range(1, hh - 1):
        for col in range(1, ww - 1):
            if m[row][col] != search[1]:
                continue
            found = 0
            for d in dirs:
                if m[row+d[0]][col+d[1]] == search[0] and m[row-d[0]][col-d[1]] == search[2]:
                    found += 1
                if found == 2:
                    n += 1
                    break
    print(n)

part1()
part2()
