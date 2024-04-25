import sys
from io import StringIO

# 重定向标准输入输出
sys.stdin = open('test_input.txt', 'r')


# 输入一个整数
n = int(input())
print(n)

# 输入一个浮点数
f = float(input())
print(f)

# 输入一个字符串
s = input().strip()
print(s)

# 输入一个整数列表
lst = list(map(int, input().split()))
print(lst)

# 输入一个逗号分隔的整数列表
lst = list(map(int, input().split(',')))
print(lst)