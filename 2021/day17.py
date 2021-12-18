def sim(vx, vy, tx, ty):
    xmin, xmax = tx
    ymin, ymax = ty
    x, y = 0, 0
    top = 0
    ok = False
    while y >= ymin and x <= xmax:
        if y > top:
            top = y
        if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
            ok = True
            break
        x += vx
        y += vy
        if vx > 0:
            vx -= 1
        vy -= 1
    return (ok, top)

def part1():
    top = 0
    tx, ty = (111, 161), (-154, -101)
    for x in range(200):
        for y in range(200):
            ok, h = sim(x, y, tx, ty)
            if ok and h > top:
                top = h
    print(top)

def part2():
    nok = 0
    tx, ty = (111, 161), (-154, -101)
    for x in range(200):
        for y in range(-200,200):
            ok, h = sim(x, y, tx, ty)
            if ok:
                nok += 1
    print(nok)

part1()
part2()
