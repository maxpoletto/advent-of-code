from lib import aodfile

badness = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
close = { '(': ')', '[': ']', '{': '}', '<': '>'}
points = { '(': 1, '[': 2, '{': 3, '<': 4 }

def part1():
    score = 0
    for l in aodfile.stripped_lines("input/input10.txt"):
        s = []
        for c in l:
            if c in '([<{':
                s.append(c)
            elif c == close[s[-1]]:
                s.pop()
            else:
                score += badness[c]
                break
    print(score)

def part2():
    scores = []
    for l in aodfile.stripped_lines("input/input10.txt"): 
        s, bad = [], False
        for c in l:
            if c in '([<{':
                s.append(c)
            elif c == close[s[-1]]:
                s.pop()
            else:
                bad = True
                break
        if bad or len(s) == 0:
            continue
        score = 0
        while len(s) > 0:
            score = score*5 + points[s.pop()]
        scores.append(score)
    scores.sort()
    print(scores[int(len(scores)/2)])

part1()
part2()
