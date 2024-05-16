from io import StringIO
import sys

inp = '''15
2 9 10 6
3 8 9 1
1 2 3 4
5 3 4 12
1 8 2 10
3 12 11 8
9 10 12 1
12 1 10 2
3 12 6 9
1 9 8 4
6 7 9 12
7 12 9 6
10 12 11 1
3 9 6 12
1 4 3 5
'''
sys.stdin = StringIO(inp)

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if (a < c < b and (d > b or d < a)) or (a < d < b and (c > b or c < a)):
        print("YES")
    else:
        print("NO")