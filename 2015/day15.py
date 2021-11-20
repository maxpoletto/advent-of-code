#!/usr/local/bin/python

import re
import collections

def score(insp, calories):
    """insp is a list of [ingredient, # of spoons] pairs. Returns the cookie
    score, a product of the sums of property scores for each ingredient.
    If 'calories' is true, returns 0 unless ingredients add to 500 calories.
    """
    global ingr
    if calories and sum([ingr[x[0]]['calories']*x[1] for x in insp ]) != 500:
        return 0
    res = 1
    for prop in ['capacity', 'durability', 'flavor', 'texture']:
        res *= max(0, sum([ingr[x[0]][prop] * x[1] for x in insp ]))
    return res

def findmax(insp, pos, spoons, calories=False):
    """Returns the maximum score possible with ingredients given by insp[pos:],
    arranged in any combination that adds up to spoons spoonfuls.
    If calories is true, ignores combinations that do not add up to 500 calories.
    """
    maxscore = 0
    if pos == len(insp)-1:
        insp[-1][1] = spoons
        return score(insp, calories)
    for i in range(0, spoons+1):
        insp[pos][1] = i
        s = findmax(insp, pos+1, spoons-i, calories)
        if s > maxscore:
            maxscore = s
    return maxscore

def part1(ingr):
    insp = [[x, 0] for x in sorted(list(ingr.keys()))]
    return findmax(insp, 0, 100)

def part2(deer):
    insp = [[x,0] for x in sorted(list(ingr.keys()))]
    return findmax(insp, 0, 100, calories=True)

fn = "input/input15.txt"
# ingr maps ingredients to their attribute values.
# E.g., Frosting -> { capacity:4, texture:0, ...}, ...
ingr = collections.defaultdict(dict)
with open(fn) as f:
    for l in f:
        i, c = l.strip().split(':')
        for c2 in re.findall(r' (\w+) ([\-\d]+)', c):
            ingr[i][c2[0]] = int(c2[1])

print(part1(ingr))
print(part2(ingr))
