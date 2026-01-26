import sys

n = int(sys.stdin.readline())
target = int(sys.stdin.readline())

dx = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dy = [0, 1, 0, -1]

grid = [[0] * n for _ in range(n)]

# 시작점
x, y = n // 2, n // 2
grid[x][y] = 1

num = 2
offset = 1  # 이동해야 할 거리 (1, 1, 2, 2, 3, 3...)
move_count = 0  # 같은 거리를 몇 번 이동했는지 체크 (2번 채우면 dist 증가)
direction = 0  # 0:상, 1:우, 2:하, 3:좌

target_x, target_y = x + 1, y + 1

while True:
    for _ in range(offset):
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위를 벗어나거나 숫자가 다 채워지면 종료
        if num > n * n:
            break

        # 좌표 갱신 및 숫자 채우기
        x, y = nx, ny
        grid[x][y] = num

        if num == target:
            target_x, target_y = x + 1, y + 1

        num += 1

    if num > n * n:
        break

    # 방향 전환
    direction = (direction + 1) % 4

    # 같은 거리로 2번 이동했으면, 이동 거리를 늘림
    move_count += 1
    if move_count == 2:
        offset += 1
        move_count = 0

for row in grid:
    print(*row)
print(target_x, target_y)
