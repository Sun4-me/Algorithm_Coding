from collections import deque


########################################################

def bfs(y, x):
    q = deque([(y, x)])
    grid[y][x] = 1
    cnt = 1
    while q:
        cy, cx = q.popleft()

        for dy, dx in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < 2 * n and 0 <= nx < 2 * m:
                if grid[ny][nx] == 0:
                    grid[ny][nx] = 1
                    q.append((ny, nx))
                    if ny % 2 == 1 and nx % 2 == 1:
                        cnt += 1

    return cnt


########################################################
# 가로 세로 | 최대 100
m, n = map(int, input().split())
# 점선의 개수
k = int(input())
# 가로 0, 번호
# 세로 1, 번호
nodes = [list(map(int, input().split())) for _ in range(k)]
########################################################
# 구상
# 가로 세로에 1로 막고 0인 거 찾기 bfs
grid = [[0] * (2 * m) for _ in range(2 * n)]
for node in nodes:
    direct, num = node[0], node[1]
    if direct == 0:
        for col in range(2 * m):
            grid[2 * num][col] = 1
    elif direct == 1:
        for row in range(2 * n):
            grid[row][2 * num] = 1

ans = []
for row in range(2 * n):
    for col in range(2 * m):
        if row % 2 == 1 and col % 2 == 1:
            if grid[row][col] == 0:
                res = bfs(row, col)
                if res <= 2 * m:
                    res = res
                else:
                    res = res
                ans.append(res)

print(max(ans))
