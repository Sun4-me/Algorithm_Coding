# 몸무게 x, 키 y (x, y)
# 둘다 커야 덩치가 큼
# 비교 불가 시 같은 등 수
# 따라서 없는 등 수도 있음
# 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1

import sys

input = sys.stdin.readline

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
res = []

for i in range(n):
    rank = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    res.append(rank)

print(*res)
