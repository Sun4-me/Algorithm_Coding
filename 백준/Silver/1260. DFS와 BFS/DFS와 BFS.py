from collections import deque
import sys

sys.setrecursionlimit(200_000)
input = sys.stdin.readline


def dfs(s):
    visited_dfs[s] = 1
    res_dfs.append(s)

    for nxt in adj[s]:
        if visited_dfs[nxt] == 0:
            dfs(nxt)


def bfs(s):
    visited_bfs = [0] * (n + 1)
    visited_bfs[s] = 1
    q = deque([s])
    res_bfs = []

    while q:
        curr = q.popleft()
        res_bfs.append(curr)

        for nxt in adj[curr]:
            if visited_bfs[nxt] == 0:
                visited_bfs[nxt] = 1
                q.append(nxt)

    return res_bfs


################
n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    adj[i].append(j)
    adj[j].append(i)
################
for row in adj:
    row.sort()
################
visited_dfs = [0] * (n + 1)
################
res_dfs = []
dfs(v)
res_bfs = bfs(v)

print(*res_dfs)
print(*res_bfs)
