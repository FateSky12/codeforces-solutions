from io import StringIO
import sys

inp = '''5

6 7
1 4
1 3
3 4
4 5
2 1
5 5
5 6

1 0

3 3
1 2
2 3
3 1

5 0

4 4
1 2
2 3
1 4
4 3
'''
sys.stdin = StringIO(inp)

# https://codeforces.com/problemset/problem/1547/G
# https://codeforces.com/contest/1547/submission/257982013
import sys
sys.setrecursionlimit(20000)

T = int(input())
for _ in range(T):
    input()
    n, m = map(int, input().split())
    # 建图
    g = [[] for _ in range(n)]
    for i in range(m):
        x, y = map(int, input().split())
        g[x - 1].append(y - 1)

    def dfs(v: int, inCycle: bool):
        inStack[v] = True
        if inCycle:
            ans[v] = -1
        else:
            ans[v] += 1
        for w in g[v]:
            if ans[w] < 0:
                continue
            if inCycle or inStack[w]:
                dfs(w, True)
            elif ans[w] < 2:
                dfs(w, False)
        inStack[v] = False

    ans = [0] * n
    inStack = [False] * n
    dfs(0, False)
    print(*ans)
    
