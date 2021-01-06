#!/opt/local/bin/python

from lib import util
import re

def winner(deer, t):
    max_dist, max_deer = 0, ""
    for d in deer:
        n = int(t/(d[2]+d[3]))
        s = n*(d[2]+d[3])
        e = min(t-s, d[2])
        dist = (n*d[2]+e)*d[1]
        if dist > max_dist:
            max_dist = dist
            max_deer = d[0]
    return (max_deer, max_dist)

def part1(deer):
    return winner(deer, 2503)[1]

def part2(deer):
    score = {}
    for d in deer:
        score[d[0]] = 0
    for t in range(1, 2504):
        score[winner(deer, t)[0]] += 1
    max_score = 0
    for d in score:
        max_score = max(max_score, score[d])
    return max_score

fn = "input/input14.txt"
deer = []
with open(fn) as f:
    for l in f:
        deer.append([ util.intorstr(x)
                    for x in re.findall(r'(\w+) can fly (\d+) km/s for (\d+) .* (\d+)', l)[0]])
print(part1(deer))
print(part2(deer))
