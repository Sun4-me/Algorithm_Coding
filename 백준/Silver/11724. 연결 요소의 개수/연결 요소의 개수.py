import sys

input = sys.stdin.readline
sys.setrecursionlimit(300000)


def dfs(x):
    visited[x] = 1

    for nxt in adj[x]:
        if visited[nxt] == 0:
            dfs(nxt)


n, m = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(m)]

adj = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

# 인접 행렬 생성
for row in nodes:
    adj[row[0]].append(row[1])
    adj[row[1]].append(row[0])

res = 0
for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i)
        res += 1

print(res)
