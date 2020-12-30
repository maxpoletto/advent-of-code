#!/opt/local/bin/python

def stripped_text(fn):
    with open(fn) as f:
        text = ''.join([x.strip() for x in f.readlines()])
    return text
