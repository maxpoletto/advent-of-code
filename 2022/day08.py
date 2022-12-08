def part1():
    m = []
    with open("input/input08.txt") as f:
        for l in f:
            m.append([ int(x) for x in l.strip()])
    nviz = 2 * len(m[0]) + 2 * len(m) - 4
    for i in range(1, len(m)-1):
        for j in range(1, len(m[0])-1):
            hidden = 0
            for ii in range(0, i):
                if m[ii][j] >= m[i][j]:
                    hidden += 1
                    break
            for ii in range(i+1, len(m)):
                if m[ii][j] >= m[i][j]:
                    hidden += 1
                    break
            for jj in range(0, j):
                if m[i][jj] >= m[i][j]:
                    hidden += 1
                    break
            for jj in range(j+1, len(m[0])):
                if m[i][jj] >= m[i][j]:
                    hidden += 1
                    break
            if hidden < 4:
                nviz += 1
    print(nviz)

def part2():
    m = []
    with open("input/input08.txt") as f:
        for l in f:
            m.append([ int(x) for x in l.strip()])
    maxview = 0
    for i in range(1, len(m)-1):
        for j in range(1, len(m[0])-1):
            view = 1
            for ii in range(i-1, -1, -1):
                if m[ii][j] >= m[i][j]:
                    break
            view *= i-ii
            for ii in range(i+1, len(m)):
                if m[ii][j] >= m[i][j]:
                    break
            view *= ii-i
            for jj in range(j-1, -1, -1):
                if m[i][jj] >= m[i][j]:
                    break
            view *= j-jj
            for jj in range(j+1, len(m[0])):
                if m[i][jj] >= m[i][j]:
                    break
            view *= jj-j
            if view > maxview:
                maxview = view
    print(maxview)

part1()
part2()
