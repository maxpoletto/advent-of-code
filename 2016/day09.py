import re
from lib import aodfile

def expand(l, rec) -> str:
    pos, cnt = 0, 0
    m = re.finditer('\((\d+)x(\d+)\)', l)
    for g in m:
        lp, rp = g.start(), g.end()
        seqlen, seqcnt = int(g.group(1)), int(g.group(2))
        if lp < pos:
            continue
        if rec:
            toexp = l[rp:rp+seqlen]
            cnt += lp-pos + expand(toexp, rec)*seqcnt
        else:
            cnt += lp-pos + seqlen*seqcnt
        pos = rp+seqlen
    if pos < len(l):
        cnt += len(l)-pos
    return cnt

def run(rec):
    lines = aodfile.stripped_lines("input/input09.txt")
    sum = 0
    for l in lines:
        sum += expand(l, rec)
    print(sum)

run(False)
run(True)
