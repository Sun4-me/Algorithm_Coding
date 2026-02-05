from collections import deque


def bfs(y, x):
    v = [0] * n
    q = deque([y])

    while q:
        curr = q.popleft()

        for i in range(n):
            if adj[curr][i] == 1:
                if v[i] == 0:
                    v[i] = 1
                    q.append(i)

    return 1 if v[x] == 1 else 0


n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
res = []

for y in range(n):
    tmp = []
    for x in range(n):
        tmp.append(bfs(y, x))
    res.append(tmp)

for i in res:
    print(*i)
