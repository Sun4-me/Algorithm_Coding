from collections import deque


##############################################################


def bfs(s):
    visited = [0] * (n + 1)
    visited[s] = 1
    q = deque([s])

    while q:
        curr = q.popleft()

        for nxt in adj[curr]:
            if visited[nxt] == 0:
                visited[nxt] = visited[curr] + 1
                q.append(nxt)

    return sum(visited)


##############################################################
n, m = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(m)]
adj = [[] for _ in range(n + 1)]
##############################################################
for row in nodes:
    adj[row[0]].append(row[1])
    adj[row[1]].append(row[0])
##############################################################
res = []
for num in range(1, n + 1):
    cnt = bfs(num)
    res.append(cnt)

print(res.index(min(res)) + 1)
