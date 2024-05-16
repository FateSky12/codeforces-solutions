from io import StringIO
import sys

inp = '''5
4
2 4 1
3
1 1
6
4 2 5 1 2
2
500
3
1 5
'''
sys.stdin = StringIO(inp)

# Accepted
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    res = []
    res.append(nums[0] + 1)
    for i, x in enumerate(nums):
        if i < n-2:
            t = (nums[i+1] - x + res[-1] - 1) // res[-1]
            if (nums[i+1] - x) % res[-1] == 0:
                t += 1
            res.append(res[-1] * t + x)
        else:
            res.append(x)
    print(*res)
