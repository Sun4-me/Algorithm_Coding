from collections import deque
from pprint import *

# 짝수 행, 홀수 행
dy = [[-1, -1, 0, 1, 1, 0], [-1, -1, 0, 1, 1, 0]]
dx = [[-1, 0, 1, 0, -1, -1], [0, 1, 1, 1, 0, -1]]


def bfs():
    v = [[0] * m for _ in range(n)]
    v[0][0] = 1
    q = deque([(0, 0)])

    while q:
        cy, cx = q.popleft()

        for k in range(6):

            if cy % 2 == 0:
                d = 0
            else:
                d = 1

            ny, nx = cy + dy[d][k], cx + dx[d][k]
            if 0 <= ny < n and 0 <= nx < m:
                if grid[ny][nx] == 0:
                    if v[ny][nx] == 0:
                        v[ny][nx] = v[cy][cx] + 1
                        q.append((ny, nx))

    return v[n - 1][m - 1] - 1


n, m, k = map(int, input().split())
grid = [[0] * m for _ in range(n)]
for _ in range(k):
    yk, xk = map(int, input().split())
    grid[yk][xk] = 1

ans = bfs()
print(ans)
