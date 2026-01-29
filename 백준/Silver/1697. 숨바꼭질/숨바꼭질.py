from collections import deque


################################################

def bfs(s, e):
    visited = [0] * 100001
    visited[s] = 1
    q = deque([s])

    while q:
        curr = q.popleft()

        if curr == e:
            return visited[curr]

        for nxt_num in [curr - 1, curr + 1, curr * 2]:
            if 0 <= nxt_num <= 100000:
                if visited[nxt_num] == 0:
                    visited[nxt_num] = visited[curr] + 1
                    q.append(nxt_num)


################################################
n, k = map(int, input().split())
################################################
res = bfs(n, k)
print(res - 1)
