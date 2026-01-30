t = int(input())
for case in range(t):
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    res = []

    for col in range(m):
        tmp = 1
        for row in range(n):
            tmp = tmp * grid[row][col]
        res.append(tmp)

    max_num = max(res)

    for i in range(m, 0, -1):
        if res[i - 1] == max_num:
            print(i)
            break
