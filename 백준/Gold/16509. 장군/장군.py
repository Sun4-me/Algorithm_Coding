from collections import deque

# 좌상하 좌상상 우상상 우상하 좌하상 좌하하 우하하 우하상
dx = [-3, -2, 2, 3, -3, -2, 2, 3]
dy = [-2, -3, -3, -2, 2, 3, 3, 2]


def check(k, y, x):
    flag = True  # 아무도없는 경우
    if k == 0 or k == 1:
        if (y + 1, x + 1) == (king_y, king_x):
            flag = False
        if (y + 2, x + 2) == (king_y, king_x):
            flag = False
    elif k == 2 or k == 3:
        if (y + 1, x - 1) == (king_y, king_x):
            flag = False
        if (y + 2, x - 2) == (king_y, king_x):
            flag = False
    elif k == 4 or k == 5:
        if (y - 1, x + 1) == (king_y, king_x):
            flag = False
        if (y - 2, x + 2) == (king_y, king_x):
            flag = False
    elif k == 6 or k == 7:
        if (y - 1, x - 1) == (king_y, king_x):
            flag = False
        if (y - 2, x - 2) == (king_y, king_x):
            flag = False

    return flag


def bfs(y, x):
    q = deque([(y, x)])
    visited[y][x] = 1

    while q:
        cy, cx = q.popleft()

        for k in range(8):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < 10 and 0 <= nx < 9:
                if visited[ny][nx] == 0 and check(k, ny, nx):
                    visited[ny][nx] = visited[cy][cx] + 1
                    q.append((ny, nx))

    return visited[king_y][king_x]


###################################
sang_y, sang_x = map(int, input().split())
king_y, king_x = map(int, input().split())
###################################
visited = [[0] * 9 for _ in range(10)]
res = bfs(sang_y, sang_x)
###################################
# 도달하지 않았다면 0일 테니까 -1로 출력됨
print(res - 1)
