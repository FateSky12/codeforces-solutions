from io import StringIO
import sys

inp = '''2
4 5
3 4
'''
sys.stdin = StringIO(inp)

# Accepted
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def merge(x, y):
    return [max(x[0], y[0]), min(x[1], y[1])]

suf = [[0, 0] for _ in range(n + 1)]
suf[n][1] = 10**9
for i in range(n - 1, 0, -1): # 这里不能是-1，因为suf[0]是无效的
    suf[i] = merge(suf[i + 1], a[i])

pre = [0, 10**9]
for i, p in enumerate(a):
    m = merge(pre, suf[i+1])
    ans = max(ans, m[1] - m[0])
    pre = merge(pre, p)

print(ans)

######################################################################################
from io import StringIO
import sys

inp = '''3
4 5
1 2
9 20
'''
sys.stdin = StringIO(inp)

# 可以通过，处理了无效区间的情况
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def merge(x, y):
    merged = [max(x[0], y[0]), min(x[1], y[1])]
    if merged[0] > merged[1]:  # Check if the merged interval is valid
        return [0, 0]  # Returning [0, 0] or any invalid interval means no valid intersection
    return merged

suf = [[0, 0] for _ in range(n + 1)]
suf[n][1] = int(1e9)  # Use int for consistency
for i in range(n - 1, -1, -1):
    suf[i] = merge(suf[i + 1], a[i])

pre = [0, int(1e9)]  # Start with a large initial valid interval
for i, p in enumerate(a):
    m = merge(pre, suf[i + 1])
    if m[0] <= m[1]:  # Check for a valid interval before calculating the length
        ans = max(ans, m[1] - m[0])
    pre = merge(pre, p)

print(ans)


