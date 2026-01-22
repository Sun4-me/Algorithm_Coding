import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(n)]

picture = [[0] * 101 for _ in range(101)]

for row in nodes:
    for i in range(row[1], row[3] + 1):
        for j in range(row[0], row[2] + 1):
            picture[i][j] += 1

cnt = 0

for row in picture:
    for num in row:
        if num > m:
            cnt += 1

print(cnt)
