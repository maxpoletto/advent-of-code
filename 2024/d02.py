def is_safe(n):
    d = n[1] - n[0]
    if abs(d) > 3 or d == 0:
        return False
    for j in range(2, len(n)):
        d2 = n[j] - n[j-1]
        if d2 * d <= 0 or abs(d2) > 3:
            return False
    return True

def part1():
    m = []
    with open("input/i02.txt") as f:
        for l in f:
            m.append(list(map(int, l.strip().split())))
        nsafe = 0
        for i in range(len(m)):
            if is_safe(m[i]):
                nsafe += 1
        print(nsafe)

def part2():
    m = []
    with open("input/i02.txt") as f:
        for l in f:
            m.append(list(map(int, l.strip().split())))
        nsafe = 0
        for i in range(len(m)):
            n = m[i]
            if is_safe(n):
                nsafe += 1
                continue
            for j in range(len(n)):
                if is_safe(n[:j] + n[j+1:]):
                    nsafe += 1
                    break
        print(nsafe)

part1()
part2()
