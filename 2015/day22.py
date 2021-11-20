#!/usr/local/bin/python

import copy
import sys

memcache = {}
def memkey(p, b) -> str:
    return '|'.join([str(p['hit']), str(p['damage']), str(p['armor']),
        str(p['mana']), str(p['shield']), str(p['poison']), str(p['recharge']),
        str(b['hit']), str(b['damage'])])
def mem(k, v) -> int:
    memcache[k] = v
    return v

def apply_effects(p, b) -> None:
    if p['shield'] > 0:
        p['shield'] -= 1
        if p['shield'] == 0:
            p['armor'] = 0
    if p['poison'] > 0:
        p['poison'] -= 1
        b['hit'] -= 3
    if p['recharge'] > 0:
        p['mana'] += 101
        p['recharge'] -= 1

def boss_move(p, b) -> None:
    if b['hit'] <= 0: # Boss is dead
        return
    apply_effects(p, b)
    p['hit'] -= max(1, b['damage']-p['armor'])

def spend(p, v) -> None:
    p['mana'] -= v
    p['spent'] += v

def cheapest_win(player, boss, e) -> int:
    k = memkey(player, boss)
    if k in memcache.keys():
        return memcache[k]

    if boss['hit'] <= 0:   # Winning state
        return mem(k, player['spent'])
    if player['hit'] <= 0: # Losing state
        return mem(k, sys.maxsize)

    if e:                  # Hack for part 2.
        player['hit'] -= 1
        if player['hit'] <= 0:
            return mem(k, sys.maxsize)

    apply_effects(player, boss)
    if boss['hit'] <= 0:   # Return early if effects killed the boss
        return mem(k, player['spent'])

    mincost = sys.maxsize

    # Try spells in turn (they are mutually exclusive in one turn).
    # First try casting every applicable effect.
    p, b = copy.copy(player), copy.copy(boss)
    if p['shield'] == 0 and p['mana'] >= 113:
        spend(p, 113)
        p['shield'] = 6
        p['armor'] += 7
        boss_move(p, b)
        mincost = min(mincost, cheapest_win(p, b, e))

    p, b = copy.copy(player), copy.copy(boss)
    if p['poison'] == 0 and p['mana'] >= 173:
        spend(p, 173)
        p['poison'] = 6
        boss_move(p, b)
        mincost = min(mincost, cheapest_win(p, b, e))

    p, b = copy.copy(player), copy.copy(boss)
    if p['recharge'] == 0 and p['mana'] >= 229:
        spend(p, 229)
        p['recharge'] = 5
        boss_move(p, b)
        mincost = min(mincost, cheapest_win(p, b, e))

    # Now cast each of the non-effect spells.
    p, b = copy.copy(player), copy.copy(boss)
    if p['mana'] >= 53: # Missile
        spend(p, 53)
        b['hit'] -= 4
        boss_move(p, b)
        mincost = min(mincost, cheapest_win(p, b, e))

    p, b = copy.copy(player), copy.copy(boss)
    if p['mana'] >= 73: # Drain
        spend(p, 73)
        b['hit'] -= 2
        p['hit'] += 2
        boss_move(p, b)
        mincost = min(mincost, cheapest_win(p, b, e))

    return mem(k, mincost)

def part1():
    player = {
        'hit': 50, 'damage': 0, 'armor': 0,
        'mana': 500, 'shield': 0, 'poison': 0,
        'recharge': 0, 'spent': 0
    }
    boss = { 'hit': 58, 'damage': 9 }
    print(cheapest_win(player, boss, False))

def part2():
    player = {
        'hit': 50, 'damage': 0, 'armor': 0,
        'mana': 500, 'shield': 0, 'poison': 0,
        'recharge': 0, 'spent': 0
    }
    boss = { 'hit': 58, 'damage': 9 }
    print(cheapest_win(player, boss, True))

part1()
memcache = {}
part2()
