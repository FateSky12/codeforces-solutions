from io import StringIO
import sys

inp = '''8
codeforces
aaaaa
xxxxy
co
d
nutdealer
mwistht
hhhhhhhhhh
'''
sys.stdin = StringIO(inp)

t = int(input())
for _ in range(t):
    s = input()
    if len(set(s)) <= 1:
        print("NO")
    else:
        print("YES")
        s = list(s)
        find = False
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] != s[j]:
                    s[i], s[j] = s[j], s[i]
                    print(''.join(s))
                    find = True
                    break
            if find:
                break