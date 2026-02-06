# 1부터 N
# N개 모두 거쳐 다시 원래로
# 한번 갔으면 못감
# 가장 적은 비용
# 비용이 0이면 못가

def dfs(now, cost, depth):
    global min_cost, start
    if cost > min_cost:
        return

    if depth == n - 1:
        if adj[now][start] > 0:
            min_cost = min(min_cost, cost + adj[now][start])
        return

    for i in range(n):
        if v[i] == 0 and adj[now][i] != 0:
            v[i] = 1
            dfs(i, cost + adj[now][i], depth + 1)
            v[i] = 0


n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
v = [0] * n
min_cost = 10 ** 10

v[0] = 1
start = 0
dfs(0, 0, 0)

print(min_cost)
