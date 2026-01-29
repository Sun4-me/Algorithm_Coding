from collections import deque

################################################
dx = [0, 0, -1, 1]  # 상 하 좌 우
dy = [-1, 1, 0, 0]

# rain도 같이 받음
def bfs(y, x, rain):
    h = grid[y][x] - rain
    q = deque([(y, x, h)])

    while q:
        cy, cx, ch = q.popleft()

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == 0:
                    nh = grid[ny][nx] - rain
                    if nh > 0:
                        visited[ny][nx] = 1
                        q.append((ny, nx, nh))


################################################
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
################################################
# 최대 높이 찾기
max_h = 0
for row in grid:
    max_h = max(max_h, max(row))
################################################

################################################
# 장마철 내리는 비의 양에 따라서 안전한 영역 개수 조사
# max_h -1 까지만 하면 된다.
res = [1]  # 아무 지역도 물에 잠기지 않을 수도 있다. 최소는 1이니까 넣어주자
for rain in range(1, max_h):
    # 비 내리는 양이 바뀔 때만 초기화
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    cnt = 0
    for row in range(n):
        for col in range(n):
            if visited[row][col] == 0 and grid[row][col] - rain > 0:
                bfs(row, col, rain)
                cnt += 1  # 안전영역 수
                res.append(cnt)
################################################
print(max(res))
