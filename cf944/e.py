from io import StringIO
import sys

inp = '''4
10 1 3
10
10
0
6
7
10 2 4
4 10
4 7
6
4
2
7
1000000000 1 1
1000000000
1000000000
99999999
6 1 3
6
5
2
6
5
'''
sys.stdin = StringIO(inp)

from bisect import bisect_right

t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    for i in range(q):
        d = int(input())
        index = bisect_right(a, d)
        if a[index-1] == d:
            print(b[index-1], end=' ')
        else:
            pre = b[index-1]
            # v = (a[index] - a[index-1]) / (b[index] - b[index-1])
            # print(pre + int((d - a[index-1]) / v), end=' ')
            print(pre + int((d - a[index-1]) * (b[index] - b[index-1]) / (a[index] - a[index-1])), end=' ')
    print()