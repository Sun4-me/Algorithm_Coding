from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1]  # 상 하 좌 우
dy = [-1, 1, 0, 0]


def bfs():
    while q:
        cur_y, cur_x = q.popleft()

        for direct in range(4):
            ny, nx = cur_y + dy[direct], cur_x + dx[direct]
            if 0 <= ny < n and 0 <= nx < m:
                if grid[ny][nx] == 0:
                    grid[ny][nx] = grid[cur_y][cur_x] + 1
                    q.append((ny, nx))


#################################################
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
#################################################
# visited 사용하지 말고 grid만 이용해보자
# q를 밖에 선언해서 1을 다 넣어버리자
q = deque()

for row in range(n):
    for col in range(m):
        if grid[row][col] == 1:
            q.append((row, col))
#################################################
bfs()
#################################################
# 토마토가 모두 익었는지 확인
res = 0
for row in grid:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit()  # -1 출력하고 끝내버리기
        res = max(res, max(row))

# 모든 토마토가 익어있으면 1이므로 0으로 잘 나옴 !
print(res - 1)
