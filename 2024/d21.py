from functools import cache

def numpad_paths():
    def pos(c):
        match c:
            case 'A': return (0, 2)
            case '0': return (0, 1)
            case _:  return ((ord(c) - ord('1')) // 3 + 1, (ord(c) - ord('1')) % 3)
    keys = ['A', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    paths = {}
    for a in keys:
        for b in keys:
            pa, pb = pos(a), pos(b)
            if pa[0] == pb[0]:
                paths[a+b] = [('>' if pa[1] < pb[1] else '<') * abs(pa[1] - pb[1])]
                continue
            elif pa[1] == pb[1]:
                paths[a+b] = [('^' if pa[0] < pb[0] else 'v') * abs(pa[0] - pb[0])]
                continue
            if pa[1] == 0 and pb[0] == 0:
                paths[a+b] = ['>' * abs(pa[1] - pb[1]) + 'v' * abs(pa[0] - pb[0])]
            elif pa[0] == 0 and pb[1] == 0:
                paths[a+b] = ['^' * abs(pa[0] - pb[0]) + '<' * abs(pa[1] - pb[1])]
            else:
                lr = ('>' if pa[1] < pb[1] else '<') * abs(pa[1] - pb[1])
                ud = ('^' if pa[0] < pb[0] else 'v') * abs(pa[0] - pb[0])
                paths[a+b] = [lr+ud, ud+lr]
    return paths

def dirpath_paths():
    pos = { 'A': (1, 2), '^': (1, 1), '<': (0, 0), 'v': (0, 1), '>': (0, 2) }
    paths = {}
    for a, pa in pos.items():
        for b, pb in pos.items():
            if pa[0] == pb[0]:
                paths[a+b] = [('>' if pa[1] < pb[1] else '<') * abs(pa[1] - pb[1])]
                continue
            elif pa[1] == pb[1]:
                paths[a+b] = [('^' if pa[0] < pb[0] else 'v')]
                continue
            if pa[1] == 0 and pb[0] == 1:
                paths[a+b] = ['>' * abs(pa[1] - pb[1]) + '^' * abs(pa[0] - pb[0])]
            elif pa[0] == 1 and pb[1] == 0:
                paths[a+b] = ['v' * abs(pa[0] - pb[0]) + '<' * abs(pa[1] - pb[1])]
            else:
                lr = ('>' if pa[1] < pb[1] else '<') * abs(pa[1] - pb[1])
                ud = ('^' if pa[0] < pb[0] else 'v')
                paths[a+b] = [lr+ud, ud+lr]
    return paths

all_paths = numpad_paths() | dirpath_paths()

@cache
def code_len(code, levels):
    if levels == 0:
        return len(code)
    l = 0
    code = 'A' + code
    for i in range(1, len(code)):
        paths = all_paths[code[i-1:i+1]]
        l += min(code_len(path + 'A', levels-1) for path in paths)
    return l

def solve(codes, levels):
    tot = 0
    for code in codes:
        tot += int(code[:-1]) * code_len(code, levels)
    print(tot)

inputs = [
    [ "029A", "980A", "179A", "456A", "379A" ],
    [ "140A", "143A", "349A", "582A", "964A" ]
]
solve(inputs[0], 3)
solve(inputs[1], 3)
solve(inputs[1], 26)
