def dfs(depth):
    global cnt
    if depth == n:
        cnt += 1
        return

    for i in range(n):
        if v1[i] == 0 and v2[i + depth] == 0 and v3[i - depth] == 0:
            v1[i] = v2[i + depth] = v3[i - depth] = 1
            dfs(depth + 1)
            v1[i] = v2[i + depth] = v3[i - depth] = 0


n = int(input())
v1 = [0] * n
v2 = [0] * (2 * n)
v3 = [0] * (2 * n)

cnt = 0
dfs(0)

print(cnt)
