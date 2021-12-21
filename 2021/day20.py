import re
from collections import defaultdict
from collections import deque
from itertools import permutations
from lib import aodfile,mat

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

def enhance(img, algo, z):
    h, w = len(img), len(img[0])
    img2 = [ ['.']*w for i in range(h) ]
    for r in range(1, h-1):
        for c in range(1, w-1):
            nb = img[r-1][c-1:c+2] + img[r][c-1:c+2] + img[r+1][c-1:c+2]
            i = parse(nb)
            img2[r][c] = algo[i]
    if z%2 == 0:
        c = '#'
    else:
        c = '.'
    img2[0] = [c]*w
    img2[1] = [c]*w
    img2[h-2] = [c]*w
    img2[h-1] = [c]*w
    for r in range(3, h-2):
        img2[r][0] = img2[r][1] = img2[r][w-2] = img2[r][w-1] = c
    return img2

def count1s(img):
    h, w = len(img), len(img[0])
    n = 0
    for r in range(2, h-2):
        for c in range(2, w-2):
            n += img[r][c] == '#'
    return n

def part1():
    algo = None
    img = []
    for l in aodfile.stripped_lines("input/input20.txt"):
        if algo is None:
            algo = l
            continue
        if l == '':
            continue
        img.append(l)
    img = pad(img, 10)
    print(mat.pp(img))
    img = enhance(img, algo, 0)
    img = enhance(img, algo, 1)
    print(mat.pp(img))
    print(count1s(img))

def part2():
    algo = None
    img = []
    for l in aodfile.stripped_lines("input/input20.txt"):
        if algo is None:
            algo = l
            continue
        if l == '':
            continue
        img.append(l)
    
    h, w = len(img), len(img[0])
    img = pad(img, 60)
    for i in range(50):
        img = enhance(img, algo, i)
    print(mat.pp(img))
    print(count1s(img))

part1()
part2()
