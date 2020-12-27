#!/opt/local/bin/python

import re
import copy

def intersect(big, small):
    res = {}
    for s in small:
        if s in big:
            res[s] = True
    return res

def prepare(menu_in):
    """Converts a list of (list-of-ingredients, list-of-allergens) pairs
    into a list of correspondings sets. Returns this list and the set (union)
    of all ingredients.
    """
    menu = []
    all_ingr = {}
    for f in menu_in:
        iset, aset = {}, {}
        for i in f[0]:
            iset[i] = True
            all_ingr[i] = True
        for a in f[1]:
            aset[a] = True
        menu.append([iset, aset])
    return menu, all_ingr

def constrain_domain(mapping):
    """Given a list of mappings of the form [ ({x1,x2,...,xn}, {y1,y2,...,ym}), ... ],
    returns a set of mappings { y1: { xi, xj, ...}, y2: { ... }, } denoting each y's
    possible x values. Each y has exactly one x. Not all x's have a y.
    """
    res = {}
    for m in mapping:
        for y in m[1]:
            if y not in res:
                res[y] = copy.copy(m[0])
            else:
                res[y] = intersect(res[y], m[0])
    return res

def part1(menu_in):
    menu, ingredients = prepare(menu_in)
    a2i = constrain_domain(menu)
    maybe_allergen = {}
    for a in a2i:
        for i in a2i[a]:
            maybe_allergen[i] = True
    for i in maybe_allergen:
        del ingredients[i]
    n = 0
    for f in menu:
        for i in f[0]:
            if i in ingredients:
                n += 1
    return n

def part2(menu_in):
    menu, _ = prepare(menu_in)
    a2i = constrain_domain(menu)
    dangerous = []
    while len(a2i) > 0:
        for a in a2i:
            if len(a2i[a]) == 1:
                # Find the allergen constrained to one ingredient.
                i = list(a2i[a].keys())[0]
                # Track ingredient and allergen.
                dangerous.append([i, a])
                # Remove this ingredient from other allergen ingredient sets.
                for a2 in a2i:
                    if a2 == a:
                        continue
                    if i in a2i[a2]:
                        del a2i[a2][i]
                # Remove this allergen.
                del a2i[a]
                break
    # Return ingredient sorted alphabetically by allergen.
    return ",".join([x[0] for x in sorted(dangerous, key=lambda x: x[1])])

fn = "input21.txt"
menu = []
with open(fn) as f:
    for l in f:
        l = l.strip()
        m = re.match(r'([\w\s]+)\(contains ([\w\s,]+)\)', l)
        if m:
            il, al = m.group(1), m.group(2)
            ingr = il.strip().split(' ')
            allerg = al.strip().split(', ')
            menu.append([ingr, allerg])

print(part1(menu))
print(part2(menu))
