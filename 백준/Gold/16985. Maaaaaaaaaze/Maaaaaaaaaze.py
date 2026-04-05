from collections import deque
from itertools import product, permutations

# --------------------------------------------

dz = [0, 0, 0, 0, -1, 1]
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]


def inb(z, y, x):
    return 0 <= z < 5 and 0 <= y < 5 and 0 <= x < 5


# --------------------------------------------

def bfs():
    v = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    v[sz][sy][sx] = 1
    q = deque([(sz, sy, sx)])

    while q:
        cz, cy, cx = q.popleft()

        if (cz, cy, cx) == (0, 4, 4):
            return v[cz][cy][cx] - 1

        for k in range(6):
            nz, ny, nx = cz + dz[k], cy + dy[k], cx + dx[k]
            if not inb(nz, ny, nx): continue
            if not real_cube[nz][ny][nx]: continue
            if v[nz][ny][nx]: continue

            v[nz][ny][nx] = v[cz][cy][cx] + 1
            q.append((nz, ny, nx))

    return 10 ** 10


# --------------------------------------------
def rotate_90(arr):
    return [lst[::-1] for lst in list(map(list, zip(*arr)))]


# --------------------------------------------
cube = []
for _ in range(5):
    board = [list(map(int, input().split())) for _ in range(5)]
    cube.append(board)
# --------------------------------------------
rotated_boards = [[[] for _ in range(4)] for _ in range(5)]
for i in range(5):
    rotated_boards[i][0] = cube[i]
    for r in range(1, 4):
        rotated_boards[i][r] = rotate_90(rotated_boards[i][r - 1])

sz, sy, sx = 4, 0, 0
ans = 10 ** 10
for p in permutations(range(5)):
    for cnt in product(range(4), repeat=5):
        real_cube = [rotated_boards[p[i]][cnt[i]] for i in range(5)]
        if real_cube[sz][sy][sx] == 0: continue
        if real_cube[0][4][4] == 0: continue

        ans = min(ans, bfs())
        if ans == 12:
            print(12)
            exit()

if ans == 10 ** 10:
    ans = -1

print(ans)
