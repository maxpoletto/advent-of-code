#!/usr/local/bin/python

from typing import List

def stripped_text(fn) -> str:
    with open(fn) as f:
        text = ''.join([x.strip() for x in f.readlines()])
    return text

def stripped_lines(fn) -> List[str]:
    lines = []
    with open(fn) as f:
        for l in f:
            lines.append(l.strip())
    return lines

def comma_separated(fn) -> List[str]:
    lines = stripped_lines(fn)
    res = []
    for l in lines:
        res += map(lambda x: x.strip(), l.split(','))
    return res
