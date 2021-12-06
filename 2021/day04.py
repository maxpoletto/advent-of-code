from lib import aodfile

def parse_input():
    nums, boards, board = [], [], []
    for l in aodfile.stripped_lines("input/input04.txt"):
        if nums == []:
            nums = list(map(lambda x: int(x), l.split(',')))
            continue
        if len(l) == 0 and len(board) > 0:
            boards.append(board)
            board = []
            continue
        if len(l) > 0:
            board.append(list(map(lambda x: [int(x), False], l.split())))
    if len(board) > 0:
        boards.append(board)
    return nums, boards

def score(board, turn):
    t = 0
    for r in board:
        for c in r:
            if c[1] == False:
                t += c[0]
    return t * turn

def num_moves(board, nums):
    def find(n):
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c][0] == n:
                    board[r][c][1] = True
                    return (r,c)
        return -1, -1
    for i in range(len(nums)):
        row, col = find(nums[i])
        if row < 0:
            continue
        ok = True
        for c in board[row]:
            if c[1] == False:
                ok = False
                break
        if ok:
            return i
        ok = True
        for r in board:
            if r[col][1] == False:
                ok = False
                break
        if ok:
            return i

def part1():
    nums, boards = parse_input()
    min_moves, min_board = 100, None
    for b in boards:
        n = num_moves(b, nums)
        if n < min_moves:
            min_moves, min_board = n, b
    print(score(min_board, nums[min_moves]))

def part2():
    nums, boards = parse_input()
    max_moves, max_board = 0, None
    for b in boards:
        n = num_moves(b, nums)
        if n > max_moves:
            max_moves, max_board = n, b
    print(score(max_board, nums[max_moves]))

part1()
part2()
