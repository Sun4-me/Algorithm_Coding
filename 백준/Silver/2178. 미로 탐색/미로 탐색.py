from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1]  # 상 하 좌 우
dy = [-1, 1, 0, 0]


def bfs(s, e):
    # 초기값 세팅
    visited = [[0] * m for _ in range(n)]
    visited[s[0]][s[1]] = 1
    q = deque([s])

    while q:
        cur = q.popleft()
        for direct in range(4):
            ny = cur[0] + dy[direct]
            nx = cur[1] + dx[direct]
            if 0 <= ny <= n - 1 and 0 <= nx <= m - 1:
                if visited[ny][nx] == 0 and grid[ny][nx] == 1:
                    visited[ny][nx] = visited[cur[0]][cur[1]] + 1
                    q.append((ny, nx))

    return visited[e[0]][e[1]]


# n: 세로, m: 가로
n, m = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(n)]

# 0, 0 에서 n-1, m-1 까지의 칸을 세도록 하자
start = (0, 0)
end = (n - 1, m - 1)

res = bfs(start, end)
print(res)
