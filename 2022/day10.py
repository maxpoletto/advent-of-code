def check_sig(x, sig, cyc):
    if (cyc + 20) % 40 == 0:
        sig += x * cyc 
    return sig

def draw(x, cyc):
    pos = (cyc - 1) % 40
    dot = '#' if pos >= x - 1 and pos <= x + 1 else '.'
    end = '\n' if cyc % 40 == 0 else ''
    print(dot, end=end)

def part1():
    x, sig, cyc = 1, 0, 1
    with open("input/input10.txt") as f:
        for l in f:
            sig = check_sig(x, sig, cyc)            
            cyc += 1
            if l.startswith("addx"):
                n = int(l.strip().split()[1])
                sig = check_sig(x, sig, cyc)
                cyc += 1
                x += n
    print(sig)

def part2():
    x, cyc = 1, 1
    with open("input/input10.txt") as f:
        for l in f:
            draw(x, cyc)            
            cyc += 1
            if l.startswith("addx"):
                n = int(l.strip().split()[1])
                draw(x, cyc)
                cyc += 1
                x += n

part1()
part2()
