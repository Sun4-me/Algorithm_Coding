import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(x):
    # 방문 표시
    visited[x] = 1

    for nxt in adj[x]:
        # 다음 탐색 할 것은 방문한 적이 없는 것
        if visited[nxt] == 0:
            dfs(nxt)


n = int(input())
edge = int(input())
nodes = [list(map(int, input().split())) for _ in range(edge)]

adj = [[] for _ in range(n + 1)]
for row in nodes:
    adj[row[0]].append(row[1])
    adj[row[1]].append(row[0])

visited = [0] * (n + 1)
dfs(1)

print(visited.count(1) - 1) # 시작지점 빼고
