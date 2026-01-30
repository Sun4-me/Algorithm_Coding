n, m = map(int, input().split())
grid_a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
grid_b = [list(map(int, input().split())) for _ in range(m)]

ans = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for p in range(m):
            ans[i][j] += grid_a[i][p] * grid_b[p][j]

for row in ans:
    print(*row)
