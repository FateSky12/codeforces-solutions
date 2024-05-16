from io import StringIO
import sys

inp = '''7
10
7
21
100
2
1000
6
'''
sys.stdin = StringIO(inp)

# Accepted
from math import gcd


t = int(input())
for _ in range(t):
    x = int(input())
    r = 0
    p = 0
    for y in range(1, x):
        s = gcd(x, y) + y
        if s > p:
            p = s
            r = y
    print(r)
