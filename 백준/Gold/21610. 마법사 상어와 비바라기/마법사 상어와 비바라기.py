import sys

input = sys.stdin.readline

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

ddy = [-1, -1, 1, 1]
ddx = [-1, 1, -1, 1]

##################################################################
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [list(map(int, input().split())) for _ in range(m)]
##################################################################
clouds = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

for d, s in commands:
    d = d - 1

    v = [[False] * n for _ in range(n)]

    # 모든 구름 d방향으로 s칸 이동
    for i in range(len(clouds)):
        clouds[i][0], clouds[i][1] = (clouds[i][0] + (dy[d] * s)) % n, (clouds[i][1] + (dx[d] * s)) % n

    # 구름이 있는 칸의 바구니 저장된 물 양 1증가
    # 방문 처리
    for y, x in clouds:
        v[y][x] = True
        grid[y][x] += 1

    for y, x in clouds:
        # 대각선 방향으로 거리가 1인 칸 수만큼 물 양 증가
        for k in range(4):
            ny, nx = y + ddy[k], x + ddx[k]
            if 0 <= ny < n and 0 <= nx < n:
                if grid[ny][nx] >= 1:
                    grid[y][x] += 1

    # 구름 삭제
    clouds = []

    for y in range(n):
        for x in range(n):
            if grid[y][x] >= 2:
                if not v[y][x]:
                    clouds.append([y, x])
                    grid[y][x] -= 2

total = 0
for y in range(n):
    for x in range(n):
        total += grid[y][x]

print(total)
