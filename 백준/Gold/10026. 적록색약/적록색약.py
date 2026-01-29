from collections import deque

################################################
dx = [0, 0, -1, 1]  # 상 하 좌 우
dy = [-1, 1, 0, 0]


def bfs(y, x):
    q = deque([(y, x)])
    visited[y][x] = 1
    color = grid[y][x]

    while q:
        cy, cx = q.popleft()

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == 0 and grid[ny][nx] == color:
                    visited[ny][nx] = 1
                    q.append((ny, nx))


################################################
n = int(input())
grid = [list(input()) for _ in range(n)]
################################################
# 적록색약이 아닌 사람 용
visited = [[0] * n for _ in range(n)]
cnt1 = 0
for row in range(n):
    for col in range(n):
        if visited[row][col] == 0:
            bfs(row, col)
            cnt1 += 1
################################################
# 적록색약 용
# 그리드의 G를 R로 바꿔버리기
for row in range(n):
    for col in range(n):
        if grid[row][col] == "G":
            grid[row][col] = "R"
visited = [[0] * n for _ in range(n)]

cnt2 = 0
for row in range(n):
    for col in range(n):
        if visited[row][col] == 0:
            bfs(row, col)
            cnt2 += 1
################################################
print(cnt1)
print(cnt2)
