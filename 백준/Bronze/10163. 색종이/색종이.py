n = int(input())
arr = [[0 for _ in range(1001)] for _ in range(1001)]

for case in range(1, n + 1):
    start_x, start_y, x, y = map(int, input().split())
    for i in range(start_y, start_y + y):
        for j in range(start_x, start_x + x):
            arr[i][j] = case

res = [0 for _ in range(n)]

for k in range(1, n + 1):
    for row in arr:
        res[k - 1] += row.count(k)

for num in res:
    print(num)