import re
from collections import deque
from lib import aodfile

def run(part):
    runq = deque() # work queue (contains names of bots ready to do work)
    conf = {}      # conf[bot][{0,1}] = [bot to receive {hi, lo} value]
    state = {}     # contains input values. len(state[bot]) = 2 -> bot to runq
    lines = aodfile.stripped_lines("input/input10.txt")

    def send(dst, val):
        if dst not in state.keys():
            state[dst] = []
        state[dst].append(val)
        if len(state[dst]) == 2:
            runq.extend([dst])

    # Parse input, build initial state.
    for l in lines:
        m = re.match('value (\d+) goes to bot (\d+)', l)
        if m:
            bot = 'b'+m.group(2)
            if bot not in state.keys():
                state[bot] = [int(m.group(1))]
            else:
                state[bot].append(int(m.group(1)))
                runq.extend([bot])
            continue
        m = re.match('bot (\d+) gives low to (\w)\w+ (\d+) and high to (\w)\w+ (\d+)', l)
        if m:
            bot = 'b'+m.group(1)
            lo, hi = m.group(2) + m.group(3), m.group(4)+m.group(5)
            conf[bot] = [lo, hi]
            continue

    # Simulate the network.
    while len(runq) > 0:
        bot = runq.popleft()
        lo, hi = conf[bot][0], conf[bot][1]
        lov, hiv = min(state[bot]), max(state[bot])
        if part == 1 and lov == 17 and hiv == 61:
            print(bot[1:])
            return
        send(lo, lov)
        send(hi, hiv)
    if part == 2:
        print(state['o0'][0] * state['o1'][0] * state['o2'][0])
    return

run(1)
run(2)
