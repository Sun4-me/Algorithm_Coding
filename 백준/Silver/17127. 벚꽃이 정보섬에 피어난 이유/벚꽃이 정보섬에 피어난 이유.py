n = int(input())
nums = list(map(int, input().split()))

prod = [[1] * n for _ in range(n)]

for i in range(n):
    p = 1
    for j in range(i, n):
        p *= nums[j]
        prod[i][j] = p

res = 0

for c1 in range(0, n - 3):
    for c2 in range(c1 + 1, n - 2):
        for c3 in range(c2 + 1, n - 1):
            s = prod[0][c1] + prod[c1 + 1][c2] + prod[c2 + 1][c3] + prod[c3 + 1][n - 1]
            res = max(res, s)

print(res)
