from io import StringIO
import sys

inp = '''5
2
3
4
5
6
'''
sys.stdin = StringIO(inp)

t = int(input())
for _ in range(t):
    n = int(input())
    