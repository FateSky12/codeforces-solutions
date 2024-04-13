# https://codeforces.com/problemset/problem/1520/D
from io import StringIO
import sys

inp = '''4
6
3 5 1 4 6 6
3
1 2 3
4
1 3 3 4
6
1 6 3 4 5 6
'''
sys.stdin = StringIO(inp)

from collections import defaultdict

def cf1520D():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        res = 0
        mp = defaultdict(int)
        for i in range(n):
            mp[a[i] - i] += 1
        for k, v in mp.items():
            res += v * (v - 1) // 2
        print(res)

cf1520D()