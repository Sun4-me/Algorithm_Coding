# [초기 상태]
# R-1, C-1
# 모든 칸에 양분이 5만큼
# M개의 나무를 구매해 땅에 심었다.
# 칸에 여러 개의 나무가 심어져 있을 수도 있다.

# [봄]
# 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
# 자기 칸에 있는 양분만 먹을 수 있음.
# 가장 나이가 어린 나무 부터 먹음
# 양분이 부족해서 못 먹으면 죽음

# [여름]
# 죽은 나무가 양분으로 변함
# 나이 // 2 를 칸에 추가

# [가을]
# 나무가 번식함
# 5의 배수인 나무만 번식하며 8방향에 나이가 1인 나무가 생김
# 땅안에서만 생김

# [겨울]
# 양분을 추가함
# A 배열만큼 추가함 R-1, C-1 조심

# [출력]
# K년이 지난 후 땅에 살아있는 나무의 개수를 구하자
import sys
from collections import deque

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

# def inb(y, x):
#     return 0 <= y < N and 0 <= x < N


# def spring(trees):
#     """나무의 성장"""
#     nxt_trees = []
#     dead_trees = []
#
#     for age, y, x in trees:
#         # 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
#         if grid[y][x] >= age:
#             grid[y][x] -= age
#             nxt_trees.append((age + 1, y, x))
#
#         # 양분이 부족해서 못 먹으면 죽음
#         else:
#             dead_trees.append((age, y, x))
#
#     return nxt_trees, dead_trees

#
# def summer(dead_trees):
#     """죽은 나무가 양분으로 변함"""
#     for age, y, x in dead_trees:
#         # 나이 // 2 를 칸에 추가
#         grid[y][x] += age // 2


# def fall(trees):
#     """나무의 번식"""
#
#     add_trees = []
#
#     for age, y, x in trees:
#         # 5의 배수인 나무만 번식
#         if age % 5 == 0:
#             for k in range(8):
#                 ny, nx = y + dy[k], x + dx[k]
#                 # 땅안에서만 생김
#                 if inb(ny, nx):
#                     # 나이가 1
#                     add_trees.append((1, ny, nx))
#
#     trees.extend(add_trees)
#
#     return trees
######################################################################
input = sys.stdin.readline
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# 나이, y-1, x-1
trees = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    C, B, D = map(int, input().split())
    trees[C - 1][B - 1].append(D)

grid = [[5] * N for _ in range(N)]
######################################################################
while K:
    make_trees = []
    dead_trees = []

    nxt_trees = [[deque() for _ in range(N)] for _ in range(N)]

    # 봄
    for y in range(N):
        for x in range(N):
            while trees[y][x]:
                age = trees[y][x].popleft()

                if grid[y][x] >= age:
                    grid[y][x] -= age
                    nxt_trees[y][x].append(age + 1)

                    if (age + 1) % 5 == 0:
                        make_trees.append((y, x))

                # 양분이 부족해서 못 먹으면 죽음
                else:
                    dead_trees.append((age, y, x))

    # 여름
    for age, y, x in dead_trees:
        # 나이 // 2 를 칸에 추가
        grid[y][x] += age // 2

    # 가을
    for y, x in make_trees:
        for k in range(8):
            ny, nx = y + dy[k], x + dx[k]
            # 땅안에서만 생김
            if 0 <= ny < N and 0 <= nx < N:
                # 나이가 1
                nxt_trees[ny][nx].appendleft(1)

    # 겨울
    for y in range(N):
        for x in range(N):
            grid[y][x] += A[y][x]

    trees = nxt_trees

    K -= 1

ans = 0
for y in range(N):
    for x in range(N):
        ans += len(trees[y][x])
print(ans)
