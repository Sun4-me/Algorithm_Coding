# [초기 정보]
# N x N 격자
# 벽이거나 비어있다.
# M 명의 승객

# [승객을 고르는 조건]
# 1) 최단 거리
# 2) 행 번호 작은 순
# 3) 열 번호 작은 순
# 4) 택시와 승객이 같은 위치에 서있으면 최단거리 0

# [연료]
# 1) 한 칸 이동 할 때마다 1 만큼 소모
# 2) 한 승객을 목적지로 성공적으로 이동 시키면
#    그 승객을 태워 이동하면서 소모한 연료 양의 두배가 충전
# 3) 이동하는 도중에 연료가 바닥나면 이동 실패 종료.
# 4) 도착과 함께 연료가 바닥 나는 경우는 괜찮다.
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def find_passenger(sy, sx):
    global power

    v = [[0] * N for _ in range(N)]
    v[sy][sx] = 1
    q = deque([(sy, sx)])

    find_person = []
    min_cnt = 0

    while q:
        cy, cx = q.popleft()

        if find_person:
            if v[cy][cx] - 1 > min_cnt:
                break

        if (cy, cx) in people:
            if not find_person:
                min_cnt = v[cy][cx] - 1
            find_person.append((cy, cx))

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if grid[ny][nx] == 0 and v[ny][nx] == 0:
                    v[ny][nx] = v[cy][cx] + 1
                    q.append((ny, nx))

    # 승객 찾았다면
    if find_person:
        power -= min_cnt

        find_person.sort()
        now_y, now_x = find_person[0]

        people.remove((now_y, now_x))

        return True, now_y, now_x

    return False, -1, -1


def go_destination(sy, sx, ey, ex):
    global power

    v = [[0] * N for _ in range(N)]
    v[sy][sx] = 1
    q = deque([(sy, sx)])

    while q:
        cy, cx = q.popleft()

        if (cy, cx) == (ey, ex):
            return v[cy][cx] - 1

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if grid[ny][nx] == 0 and v[ny][nx] == 0:
                    v[ny][nx] = v[cy][cx] + 1
                    q.append((ny, nx))

    return -1


#########################################################
N, M, power = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

a, b = map(int, input().split())
start_y, start_x = a - 1, b - 1

people = set()
people_want_go = dict()

for _ in range(M):
    sy, sx, ty, tx = map(int, input().split())
    people.add((sy - 1, sx - 1))
    people_want_go[(sy - 1, sx - 1)] = (ty - 1, tx - 1)
#########################################################
cy, cx = start_y, start_x
# print(go_destination(cy, cx))
# print(people)

while True:
    if not people:
        break

    if power <= 0:
        power = -1
        break

    is_find, now_y, now_x = find_passenger(cy, cx)

    if not is_find:
        if people:
            power = -1
        break

    if is_find:
        if power <= 0:
            power = -1
            break

        target_y, target_x = people_want_go[now_y, now_x]
        length = go_destination(now_y, now_x, target_y, target_x)

        if length == -1:
            power = -1
            break

        power -= length

        if power < 0:
            power = -1
            break

        power += length * 2
        cy, cx = target_y, target_x

# print(cy, cx)
print(power)
