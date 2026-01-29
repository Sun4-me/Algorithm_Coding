from collections import deque
import sys

input = sys.stdin.readline


def bfs(s):
    visited = [0] * (n + 1)
    visited[s] = 1
    cnt = 1
    q = deque([s])

    while q:
        cur = q.popleft()

        for nxt in adj[cur]:
            if visited[nxt] == 0:
                cnt += 1
                visited[nxt] = cnt
                q.append(nxt)

    return visited


n, m, r = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(m)]
adj = [[] for _ in range(n + 1)]

for row in nodes:
    adj[row[0]].append(row[1])
    adj[row[1]].append(row[0])

for row in adj:
    row.sort(reverse=True)

res = bfs(r)

for i in res[1:]:
    print(i)
