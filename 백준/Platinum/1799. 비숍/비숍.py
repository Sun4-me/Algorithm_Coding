def dfs(cells, idx, count):
    global ans

    # 지금까지 놓은 수에 앞으로 남은 칸 수를 다 비숍을 넣어도 최대값 보다 작다면
    if count + (len(cells) - idx) <= ans:
        return

        # 가능한 칸 다 확인한 경우
    if idx == len(cells):
        ans = max(ans, count)
        return

    y, x = cells[idx]

    # [1] 비숍을 놓는 경우
    # 두 대각선 배열 확인
    if not v1[y - x + n] and not v2[y + x]:
        v1[y - x + n] = True
        v2[y + x] = True
        dfs(cells, idx + 1, count + 1)
        v1[y - x + n] = False
        v2[y + x] = False

    # [2] 안 넣는 경우
    dfs(cells, idx + 1, count)


##############################################################
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
##############################################################
white = []
black = []

for y in range(n):
    for x in range(n):
        if grid[y][x] == 1:
            if (y + x) % 2 == 0:
                white.append((y, x))
            else:
                black.append((y, x))
##############################################################
v1 = [False] * (2 * n)  # 우하향
v2 = [False] * (2 * n)  # 우상향
##############################################################
ans = 0
res = 0
dfs(white, 0, 0)
res += ans

ans = 0
dfs(black, 0, 0)
res += ans

print(res)
