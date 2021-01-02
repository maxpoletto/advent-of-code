#!/opt/local/bin/python

def intorstr(x):
    try:
        return int(x)
    except ValueError:
        return x
