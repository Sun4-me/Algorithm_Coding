def cal(i, j, x, y):
    area = [row[j:y] for row in grid[i:x]]
    sm = 0
    for row in area:
        sm += sum(row)

    return sm


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(cal(i - 1, j - 1, x, y))
