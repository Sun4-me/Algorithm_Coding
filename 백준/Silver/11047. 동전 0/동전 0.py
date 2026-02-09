n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

ans = 0

for i in range(n - 1, -1, -1):
    # 큰 가치 부터 작은 가치 순으로
    count = k // coins[i]
    # 갱신
    k = k - (coins[i] * count)
    ans += count

print(ans)
