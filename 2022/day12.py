
def parse():
    m = []
    with open('input/input12.txt') as f:
        for l in f:
            m.append([ord('z')+2] + [ord(c) for c in l.strip()] + [ord('z')+2])
    m = [[ord('z')+2] * len(m[0])] + m + [[ord('z')+2] * len(m[0])]
    S, E = None, None
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == ord('S'):
                S = (i, j)
                m[i][j] = ord('a')
            elif m[i][j] == ord('E'):
                E = (i, j)
                m[i][j] = ord('z')

    maxdist = len(m) * len(m[0])
    d = [ [maxdist] * len(m[0]) for _ in range(len(m)) ]
    return m, d, S, E

def part1():
    m, d, S, E = parse()
    # BFS from S to E
    d[S[0]][S[1]] = 0
    q = [S]
    while q:
        i, j = q.pop(0)
        if (i, j) == E:
            print(d[i][j])
            break
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if m[ni][nj] > m[i][j] + 1:
                continue
            if d[ni][nj] > d[i][j] + 1:
                d[ni][nj] = d[i][j] + 1
                q.append((ni, nj))

def part2():
    m, d, _, E = parse()
    # BFS from E to all nodes with 'a'
    d[E[0]][E[1]] = 0
    q = [E]
    mindist = len(m) * len(m[0])
    while q:
        i, j = q.pop(0)
        if m[i][j] == ord('a'):
            mindist = min(mindist, d[i][j])
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if m[ni][nj] < m[i][j] - 1 or m[ni][nj] > ord('z'):
                continue
            if d[ni][nj] > d[i][j] + 1:
                d[ni][nj] = d[i][j] + 1
                q.append((ni, nj))
    print(mindist)

part1()
part2()
