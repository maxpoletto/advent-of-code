def getnum(s : str) -> int:
    i = 0
    for c in s:
        if c in '0123456789':
            i = int(c) * 10
            break
    for c in reversed(s):
        if c in '0123456789':
            i += int(c)
            break
    return i

def getwordnum(s : str) -> int:
    n = 0
    for i in range(len(s)):
        if s[i] in '0123456789':
            n = int(s[i])
            break
        if s[i] not in 'otfsen':
            continue
        if s[i:].startswith('one'):
            n = 1
        elif s[i:].startswith('two'):
            n = 2
        elif s[i:].startswith('three'):
            n = 3
        elif s[i:].startswith('four'):
            n = 4
        elif s[i:].startswith('five'):
            n = 5
        elif s[i:].startswith('six'):
            n = 6
        elif s[i:].startswith('seven'):
            n = 7
        elif s[i:].startswith('eight'):
            n = 8
        elif s[i:].startswith('nine'):
            n = 9
        else:
            continue
        break
    n *= 10

    for i in reversed(range(len(s))):
        if s[i] in '0123456789':
            n += int(s[i])
            break
        if s[i] not in 'eorxnt':
            continue
        if s[:i+1].endswith('one'):
            n += 1
        elif s[:i+1].endswith('two'):
            n += 2
        elif s[:i+1].endswith('three'):
            n += 3
        elif s[:i+1].endswith('four'):
            n += 4
        elif s[:i+1].endswith('five'):
            n += 5
        elif s[:i+1].endswith('six'):
            n += 6
        elif s[:i+1].endswith('seven'):
            n += 7
        elif s[:i+1].endswith('eight'):
            n += 8
        elif s[:i+1].endswith('nine'):
            n += 9
        else:
            continue
        break
    return n

def count(func):
    with open('input/i01.txt') as f:
        tot = 0
        for l in f:
            n = func(l.strip())
            tot += n
        print(tot)

count(getnum)
count(getwordnum)
