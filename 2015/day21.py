#!/usr/local/bin/python

import itertools

weapons = {
    'Dagger':     [  8, 4, 0 ],
    'Shortsword': [ 10, 5, 0 ],
    'Warhammer':  [ 25, 6, 0 ],
    'Longsword':  [ 40, 7, 0 ],
    'Greataxe':   [ 74, 8, 0 ],
}
armors = {
    'None':       [  0, 0, 0 ],
    'Leather':    [ 13, 0, 1 ],
    'Chainmail':  [ 31, 0, 2 ],
    'Bandedmail': [ 75, 0, 4 ],
    'Platemail': [ 102, 0, 5 ],
    'Splintmail': [ 53, 0, 3 ],
}
rings = {
    'Damage +1':  [ 25, 1, 0 ],
    'Damage +2':  [ 50, 2, 0 ],
    'Damage +3': [ 100, 3, 0 ],
    'Defense +1': [ 20, 0, 1 ],
    'Defense +2': [ 40, 0, 2 ],
    'Defense +3': [ 80, 0, 3 ],
}
ringslist = [()] + [(k,) for k in rings.keys()] + [p for p in itertools.combinations(rings, 2)]

def turn(attacker, defender):
    damage = max(attacker['d'] - defender['a'], 1)
    defender['h'] -= damage

def defeats(player, boss):
    while True:
        turn(player, boss)
        if boss['h'] <= 0:
            return True
        turn(boss, player)
        if player['h'] <= 0:
            return False

def evaluate(predicate):
    for weapon in weapons.keys():
        for armor in armors.keys():
            for rr in ringslist:
                b = { 'h': 104, 'd': 8, 'a': 1}
                s = { 'h': 100, 'd': weapons[weapon][1], 'a': armors[armor][2] }
                setup = " ".join([weapon, armor, str(rr)])
                cost = weapons[weapon][0] + armors[armor][0]
                for r in rr:
                    cost += rings[r][0]
                    s['d'] += rings[r][1]
                    s['a'] += rings[r][2]
                predicate(s, b, cost, setup)

def part1():
    mincost = 10000
    minsetup = ""
    def f(s, b, cost, setup):
        nonlocal mincost
        nonlocal minsetup
        if defeats(s, b) and cost < mincost:
            mincost = cost
            minsetup = setup
    evaluate(f)
    print("Min cost =", mincost, "with", minsetup)

def part2():
    maxcost = 0
    maxsetup = ""
    def g(s, b, cost, setup):
        nonlocal maxcost
        nonlocal maxsetup
        if (not defeats(s, b)) and cost > maxcost:
            maxcost = cost
            maxsetup = setup
    evaluate(g)
    print("Max cost =", maxcost, "with", maxsetup)

part1()
part2()
