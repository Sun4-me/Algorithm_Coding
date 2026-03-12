# [수의 위치]
# 반지름 i. 1<=1<=N
# 그 원판을 i번째 원판이라고 함
# M개의 정수가 적혀있고, i번째 원판에 적힌 j번째 수의 위치는 (i, j)라고 표현

# [수의 위치 인접 조건]
# 1) i 원판의 첫 번째(1)는 두 번째와 마지막 번째(M)와 인접하다.
# 2) 마지막 번째(M)은 마지막에서 두번째(M-1)와 첫번째(1)와 인접하다.
# 3) i 원판의 j번째 수는 j-1과 j+1과 인접하다. (2 <= j <= M-1)
# 4) 첫 번째 원판의 j번째 수는 두번째 원판의 j와 인접하다.
# 5) 마지막 번째(N) 원판의 j번째 수는 마지막에서 두번째(M-1)의 j번째 수와 인접하다.
# 6) i번째 원판의 j번째는  (i-1, j), (i+1, j)와 인접하다. (2 ≤ i ≤ N-1)

# [회전 방법]
# 총 T번 화전한다.
# x, d, k
# 1) 번호가 x의 배수인 원판을 d방향으로 k칸 회전
# d: 0 시계 방향 | d: 1 반시계 방향
# 2) 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
#   2-1) 그러한 수가 있는 경우, 원판에서 인접하면서 같은 수를 모두 지운다.
#   2-2) 없는 경우, 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수는 1을 빼고 작은 수는 1을 더한다.

# [결과 값]
# T번 회전 시킨 후 원판에 적힌 수의 합을 구하자.
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def inb(y, x):
    return 1 <= y < N + 1 and 0 <= x < M


def circle_rotate(x, d, k):
    """x의 배수인 원판들을 d방향으로 k칸만큼 돌린다."""

    target_idx = [idx for idx in range(1, N + 1) if idx % x == 0]

    for idx in target_idx:
        coord[idx].rotate(d * k)


def bfs(sy, sx, num):
    global is_deleted

    v[sy][sx] = True
    q = deque([(sy, sx)])

    remove_target = [(sy, sx)]

    while q:
        cy, cx = q.popleft()

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if not inb(ny, nx):
                if nx == -1:  # 좌
                    nx = M - 1
                elif nx == M:  # 우
                    nx = 0
                else:
                    continue

            if coord[ny][nx] == num:
                if not v[ny][nx]:
                    v[ny][nx] = True
                    remove_target.append((ny, nx))
                    q.append((ny, nx))

    if len(remove_target) >= 2:
        is_deleted = True
        for y, x in remove_target:
            coord[y][x] = 0


#########################################################
N, M, T = map(int, input().split())
coord = [deque([0] * M)]
for _ in range(N):
    line = deque(map(int, input().split()))
    coord.append(line)

command = []
for _ in range(T):
    xi, di, ki = list(map(int, input().split()))
    di = 1 if di == 0 else -1
    command.append([xi, di, ki])

#########################################################
for cmd in command:
    # print("Phase", step, "초기 상태")
    # for row in coord:
    #     print(*row)
    # print()

    circle_rotate(*cmd)

    # print("회전 후")
    # for row in coord:
    #     print(*row)
    # print()

    v = [[False] * M for _ in range(N + 1)]
    for i in range(M):
        v[0][i] = True

    # 지운 경우
    is_deleted = False
    total = 0
    cnt = 0

    for y in range(1, N + 1):
        for x in range(M):
            total += coord[y][x]
            if not v[y][x] and coord[y][x] != 0:
                cnt += 1
                bfs(y, x, coord[y][x])

    # print("bfs 후")
    # for row in coord:
    #     print(*row)
    # print()

    # 없는 경우, 원판에 적힌 수의 평균을 구하고,
    # 평균보다 큰 수는 1을 빼고 작은 수는 1을 더한다.
    if not is_deleted:
        if cnt != 0:
            average = total / cnt

            for y in range(1, N + 1):
                for x in range(M):
                    if coord[y][x] == 0:
                        continue

                    if coord[y][x] > average:
                        coord[y][x] -= 1

                    elif coord[y][x] < average:
                        coord[y][x] += 1

            # print("제거한 수가 없어서 평균 구해서 한 경우")
            # for row in coord:
            #     print(*row)
            # print()
            #
            # print("현재 평균", average)


print(sum(sum(row) for row in coord))
