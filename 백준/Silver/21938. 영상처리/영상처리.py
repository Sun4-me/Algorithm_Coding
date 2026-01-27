import sys

sys.setrecursionlimit(300000)
input = sys.stdin.readline

dx = [1, 0, -1, 0]  # 우 하 좌 상
dy = [0, 1, 0, -1]


def dfs(y, x):
    # 방문 갱신
    visited[y][x] = 1

    for direct in range(4):
        nx = x + dx[direct]
        ny = y + dy[direct]
        if (0 <= nx <= m - 1) and (0 <= ny <= n - 1):
            if visited[ny][nx] == 0 and new_picture[ny][nx] == 255:
                dfs(ny, nx)


n, m = map(int, input().split())
raw_picture = [list(map(int, input().split())) for _ in range(n)]
t = int(input())

visited = [[0] * m for _ in range(n)]

# 새로운 그림 그리기
new_picture = [[] for _ in range(n)]
for row in range(n):
    for col in range(0, 3 * m, 3):
        if (raw_picture[row][col] + raw_picture[row][col + 1] + raw_picture[row][col + 2]) / 3 >= t:
            new_picture[row].append(255)
        else:
            new_picture[row].append(0)

res = 0
# 물체 개수 세기
for row in range(n):
    for col in range(m):
        if new_picture[row][col] == 255 and visited[row][col] != 1:
            dfs(row, col)
            res += 1

print(res)
