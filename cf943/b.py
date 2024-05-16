from io import StringIO
import sys

inp = '''6
5 4
10011
1110
3 3
100
110
1 3
1
111
4 4
1011
1111
3 5
100
11010
3 1
100
0
'''
sys.stdin = StringIO(inp)

# Accepted
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a, b = input(), input()
    # print(n, m, a, b)

    i, j = 0, 0
    while i < n and j < m:
        if a[i] == b[j]:
            i += 1
            j += 1
            continue
        j += 1
    print(i)

