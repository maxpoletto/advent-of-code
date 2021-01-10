#!/opt/local/bin/python

import re

def intorstr(x):
    """If x is an int, returns its numeric value. Else returns x unchanged."""
    try:
        return int(x)
    except ValueError:
        return x

def subiter(pat, repl, s):
    """Iterator yielding the result of replacing pat with repl in s, one
    occurrence at a time.
    """
    for m in re.finditer(pat, s):
        yield s[:m.start()] + repl + s[m.end():]
