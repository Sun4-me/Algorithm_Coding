n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

res = 0
for i in coins:
    if k >= i:
        res += k // i
        k %= i
        if k <= 0:
            break

print(res)
