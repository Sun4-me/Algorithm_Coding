n = int(input())
nums = list(map(int, input().split()))
t, p = map(int, input().split())

t_cnt = 0

for i in nums:
    t_cnt += (i + t - 1) // t

print(t_cnt)
print(n // p, n % p)
