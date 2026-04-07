from collections import deque

# ------------------------------------------

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def inb(y, x):
    return 0 <= y < H and 0 <= x < W


# ------------------------------------------

def bfs():
    while q:
        cy, cx = q.popleft()

        if energy[cy][cx] == 1: continue

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if not inb(ny, nx): continue
            if grid[ny][nx] == 1 and energy[cy][cx] - 1 > energy[ny][nx]:
                energy[ny][nx] = energy[cy][cx] - 1
                q.append((ny, nx))

            elif grid[ny][nx] == -1 and energy[cy][cx] - 1 >= 1:
                grid[ny][nx] = 99


# ------------------------------------------
W, H = map(int, input().split())
N = int(input())
grid = [[0] * W for _ in range(H)]

target = []
for _ in range(N):
    a, x, y = input().split()
    if a == "redstone_dust":
        grid[int(y)][int(x)] = 1
    elif a == "redstone_block":
        grid[int(y)][int(x)] = 2
    elif a == "redstone_lamp":
        grid[int(y)][int(x)] = -1
        target.append((int(y), int(x)))

energy = [[0] * W for _ in range(H)]

q = deque()

for y in range(H):
    for x in range(W):
        if grid[y][x] == 1:
            q.append((y, x))
        elif grid[y][x] == 2:
            energy[y][x] = 15
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if not inb(ny, nx): continue
                energy[ny][nx] = 15
                if grid[ny][nx] == -1:
                    grid[ny][nx] = 99

# ------------------------------------------
bfs()
# ------------------------------------------
for y, x in target:
    if grid[y][x] != 99:
        print("failed")
        break

else:
    print("success")
