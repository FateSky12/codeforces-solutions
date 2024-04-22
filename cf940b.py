n = int(input())
k = int(input())
A = int(input())
B = int(input())

res = 0
while n > 1:
    res += (n % k) * A
    n -= n % k
    if (n - n // k) * A <= B:
        res += (n - 1) * A
        break
    res += B
    n //= k
print(res)