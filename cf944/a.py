from io import StringIO
import sys

inp = '''10
1 9
8 4
1 4
3 4
2 0
2 4
6 9
3 3
0 0
9 9
'''
sys.stdin = StringIO(inp)



t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x < y:
        print(x, y)
    else:
        print(y, x)