from io import StringIO
import sys

inp = '''4
1 3 2 4
4 2 3 1
'''
sys.stdin = StringIO(inp)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
pos = [-1] * (n + 1)
for i, v in enumerate(a):
    pos[v] = i
cnt = [0] * n
for i, v in enumerate(b):
    d = (pos[v] - i + n) % n
    cnt[d] += 1
print(max(cnt))