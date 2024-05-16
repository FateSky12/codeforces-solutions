n, d = map(int, input().split())
nums = list(map(int, input().split()))

res = 0
i = 0
for k in range(n):
    while nums[i] + d < nums[k]:
        i += 1
    res += (k - i) * (k - i - 1) // 2
print(res)