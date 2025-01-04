def read_input():
    with open("input/i10.txt") as f:
        m = [list(map(int, list(l.strip()))) for l in f]
    trailheads = [(r, c) for r in range(len(m)) for c in range(len(m[0])) if m[r][c] == 0]
    return m, trailheads

def find_summits(m, th, all_paths):
    explored = set({th})
    q = [th]
    summits = []
    while q:
        r, c = q.pop(0)
        if m[r][c] == 9:
            summits.append((r, c))
            continue
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= len(m) or nc < 0 or nc >= len(m[0]):
                continue
            if m[nr][nc] - m[r][c] == 1 and (nr, nc) not in explored:
                if not all_paths:
                    explored.add((nr, nc))
                q.append((nr, nc))
    return len(summits)

def count(all_paths):
    m, trailheads = read_input()
    print(sum([find_summits(m, th, all_paths) for th in trailheads]))

count(False) # Part 1
count(True) # Part 2
