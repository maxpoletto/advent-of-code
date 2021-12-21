from lib import aodfile

def pad(img, n):
    h, w = len(img), len(img[0])
    res = [ ['.']*(w+2*n) for i in range(n) ]
    for i in img:
        res.append(['.'] * n + [c for c in i] + ['.']*n)
    res += [ ['.']*(w+2*n) for i in range(n) ]
    return res

def parse(nb):
    n = 0
    for i in range(9):
        n *= 2
        n += (nb[i] == '#')
    return n

def enhance1(img, algo, parity):
    h, w = len(img), len(img[0])
    img2 = [ ['.']*w for i in range(h) ]
    for r in range(1, h-1):
        for c in range(1, w-1):
            nb = img[r-1][c-1:c+2] + img[r][c-1:c+2] + img[r+1][c-1:c+2]
            i = parse(nb)
            img2[r][c] = algo[i]
    if algo[0] == '#':
        c = '#.'[parity%2]
        img2[0] = [c]*w
        img2[1] = [c]*w
        img2[h-2] = [c]*w
        img2[h-1] = [c]*w
        for r in range(2, h-2):
            img2[r][0] = img2[r][1] = img2[r][w-2] = img2[r][w-1] = c
    return img2

def enhance(img, algo, n):
    img = pad(img, n+2)
    for i in range(n):
        img = enhance1(img, algo, i)
    return img

def count1s(img):
    h, w = len(img), len(img[0])
    n = 0
    for r in range(1, h-1):
        for c in range(1, w-1):
            n += img[r][c] == '#'
    return n

algo = None
img = []
for l in aodfile.stripped_lines("input/input20.txt"):
    if algo is None:
        algo = l
        continue
    if l == '':
        continue
    img.append(l)

# part 1
img2 = enhance(img, algo, 2)
print(count1s(img2))
# part 2
img2 = enhance(img, algo, 50)
print(count1s(img2))
