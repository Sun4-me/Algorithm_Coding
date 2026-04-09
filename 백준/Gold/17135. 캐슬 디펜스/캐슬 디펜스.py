from itertools import combinations


# -------------------------------------------

def inb(y, x):
    return 0 <= y < N and 0 <= x < M


def dist(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)


# -------------------------------------------

def gravity():
    for x in range(M):
        grid[N - 1][x] = 0

    for y in range(N - 2, -1, -1):
        for x in range(M):
            grid[y + 1][x] = grid[y][x]

    for x in range(M):
        grid[0][x] = 0


# -------------------------------------------
N, M, D = map(int, input().split())
ori_grid = [list(map(int, input().split())) for _ in range(N)]
# -------------------------------------------
possible = [(N, x) for x in range(M)]

ans = 0
for combi in combinations(possible, 3):
    grid = [row[:] for row in ori_grid]
    res = 0
    while True:
        if sum(sum(row) for row in grid) == 0: break
        target = set()
        for cy, cx in combi:
            do_your_job = False
            for y in range(N - 1, -1, -1):
                if do_your_job: break
                temp = []
                for y in range(N):
                    for x in range(M):
                        if grid[y][x] == 1:
                            d = dist(cy, cx, y, x)
                            if d <= D:
                                temp.append((d, x, y))

                if temp:
                    temp.sort()  #
                    ty, tx = temp[0][2], temp[0][1]
                    target.add((ty, tx))

        for r, c in target:
            grid[r][c] = 0
            res += 1

        gravity()

    ans = max(ans, res)
# -------------------------------------------
print(ans)
