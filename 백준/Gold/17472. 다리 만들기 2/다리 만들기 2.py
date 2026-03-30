from collections import deque, defaultdict

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# ===============================================================

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        p[y] = x

    else:
        p[x] = y


# ===============================================================
def inb(y, x):
    return 0 <= y < N and 0 <= x < M


def make_island(y, x, num, idx):
    v[y][x] = True
    q = deque([(y, x)])
    coord = [(y, x)]

    while q:
        cy, cx = q.popleft()

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if not inb(ny, nx): continue
            if v[ny][nx]: continue
            if grid[ny][nx] == num:
                v[ny][nx] = True
                q.append((ny, nx))
                coord.append((ny, nx))

    island[idx].extend(coord)
    return coord


def make_bridge(coord, num):
    for y, x in coord:
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            dist = 0

            while inb(ny, nx):

                # 1. 같은 섬을 만나면 다리를 놓을 수 없으므로 종료
                if grid[ny][nx] == num:
                    break

                # 2. 바다면 다리 길이를 늘리고 계속 직진
                elif grid[ny][nx] == 0:
                    dist += 1
                    ny += dy[k]
                    nx += dx[k]
                # 3. 다른 섬을 만난 경우
                else:
                    # 다리 길이가 2 이상일 때만 유효한 다리로 추가
                    if dist >= 2:
                        bridge.append([num, grid[ny][nx], dist])
                    break  # 섬에 닿았으니 더 이상 뚫고 가지 않고 직진 종료


# ===============================================================
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
# ===============================================================

# [0] 섬 제작
island = defaultdict(list)
v = [[False] * M for _ in range(N)]
idx = 1

for y in range(N):
    for x in range(M):
        if grid[y][x] == 1 and not v[y][x]:
            coord = make_island(y, x, grid[y][x], idx)
            for ty, tx in coord:
                grid[ty][tx] = idx
            idx += 1

max_num = idx - 1  # 총 섬의 개수
# ===============================================================

# [1] 다리 제작
bridge = []
for i in range(1, max_num + 1):
    make_bridge(island[i], i)

# ===============================================================
# [2] 최소 스패닝 트리
bridge.sort(key=lambda x: x[2])
p = [i for i in range(max_num + 1)]

ans = 0
for a, b, w in bridge:
    if find(a) != find(b):
        union(a, b)
        ans += w

# ===============================================================

# [3] 엄마 아빠 확인
parent = find(1)
for i in range(2, max_num + 1):
    if find(i) != parent:
        ans = -1
        break

if ans == 0: ans = -1

print(ans)
