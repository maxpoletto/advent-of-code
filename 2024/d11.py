from collections import Counter
from typing import Counter as CounterType

def blink(c : CounterType) -> CounterType:
    c2 = Counter()
    for k, v in c.items():
        if k == 0:
            c2.update({1: v})
        elif len(str(k)) % 2 == 0:
            l = len(str(k)) // 2
            a, b = int(str(k)[:l]), int(str(k)[l:])
            c2.update({a: v})
            c2.update({b: v})
        else:
            c2.update({2024*k: v})
    return c2

def count(n):
    with open("input/i11.txt") as f:
        c = Counter({ k: 1 for k in map(int, f.readline().split()) })
    for i in range(n):
        c = blink(c)
    print(sum(v for v in c.values()))

count(25)
count(75)
