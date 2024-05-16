from io import StringIO
import sys

inp = '''6
11010
00000000
1
10
0001111
0110
'''
sys.stdin = StringIO(inp)


t = int(input())
for _ in range(t):
    s = input()
    if '0' not in s or '1' not in s:
        print(1)
        continue
    else:
        pz = False
        res = 0
        pre = s[0]
        for i, c in enumerate(s):
            if pre == '0' and c == '1':
                pz = True
            if c != pre:
                res += 1
                pre = c
        if pz:
            print(res)
        else:
            print(res+1)