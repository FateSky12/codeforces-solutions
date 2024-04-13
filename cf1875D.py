# https://codeforces.com/problemset/problem/1875/D
from io import StringIO
import sys

inp = """4
8
5 2 1 0 3 0 4 0
2
1 2
5
1 0 2 114514 0
8
0 1 2 0 1 2 0 3
"""
sys.stdin = StringIO(inp)

def cf1875D():
    t = int(input())
    for i in range(t):
        n = int(input())
        cnt = [0] * (n + 1)
        vs = list(map(int, input().split()))
        print(vs)
        for v in vs:
            if v < n:
                cnt[v] += 1
        mex = 0
        while cnt[mex] > 0:
            mex += 1
        ans = mex * (cnt[0] - 1)
        f = [0] * mex
        for i in range(1, mex):
            f[i] = 1e9
            for j, c in enumerate(cnt[:i]):
                f[i] = min(f[i], f[j] + i * c)
            ans = min(ans, f[i] + mex * (cnt[i] - 1))
        print(ans)

cf1875D()