import sys

input = sys.stdin.readline
sys.setrecursionlimit(300000)


def dfs(x):
    global order
    # 방문 체크
    visited[x] = order
    order += 1

    for nxt in adj[x]:
        if visited[nxt] == 0:
            dfs(nxt)


n, m, r = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(m)]

adj = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

# 인접 행렬 생성
for row in nodes:
    adj[row[0]].append(row[1])
    adj[row[1]].append(row[0])

# 오름 차순
for row in adj:
    row.sort()

order = 1
dfs(r)

for i in range(1, n + 1):
    print(visited[i])
