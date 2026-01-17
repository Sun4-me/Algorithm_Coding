nums = list(map(int, input().split()))

res = 0

for i in nums:
    res += i**2

print(res % 10)
