def dfs(depth, cy, cx):
    global ans
    if alpha_used.count(2) == 1:
        return

    ans = max(ans, depth)


    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < n and 0 <= nx < m:
            if v[ny][nx] == 0:
                v[ny][nx] = 1
                alpha_used[ord(grid[ny][nx]) - ord("A")] += 1
                dfs(depth + 1, ny, nx)
                v[ny][nx] = 0
                alpha_used[ord(grid[ny][nx]) - ord("A")] -= 1


n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

v = [[0] * m for _ in range(n)]
v[0][0] = 1
alpha_used = [0] * 26
alpha_used[ord(grid[0][0]) - ord("A")] += 1
ans = 0

dfs(1, 0, 0)
print(ans)
