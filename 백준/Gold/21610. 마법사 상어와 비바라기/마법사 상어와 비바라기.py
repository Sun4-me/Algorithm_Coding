#############################################################
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

ddy = [-1, -1, 1, 1]
ddx = [-1, 1, -1, 1]
#############################################################
#############################################################
# 격자 크기, 키우는 년수
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
command = [list(map(int, input().split())) for _ in range(M)]
#############################################################
# 초기 영양제의 위치
special = [[N - 1, 0], [N - 2, 0], [N - 1, 1], [N - 2, 1]]

for cmd in command:
    # 영양제 투입 여부 배열
    v = [[0] * N for _ in range(N)]

    # 이동 방향, 이동 칸수
    d, p = cmd[0] - 1, cmd[1]

    # 현재 영양제의 수
    length = len(special)

    # 특수 영양제 이동
    for i in range(length):
        cy, cx = special[i][0], special[i][1]

        # 지구처럼 돌아오니까 처리
        ny, nx = (cy + (dy[d] * p)) % N, (cx + (dx[d] * p)) % N

        # 이동 갱신
        special[i][0], special[i][1] = ny, nx

        # 방문 처리
        v[ny][nx] = 1

    # [2] (현재 높이 +1) 특수 영양제 투입된 나무 성장 시키기
    for i in range(length):
        cy, cx = special[i][0], special[i][1]
        grid[cy][cx] += 1

    # [2] (대각선) 특수 영양제 투입된 나무 성장 시키기
    for i in range(length):
        cy, cx = special[i][0], special[i][1]
        # 대각선으로 인접한 방향에 높이가 1 이상인 리브로수 찾기

        cnt = 0  # 성장할 높이
        for k in range(4):
            ny, nx = cy + ddy[k], cx + ddx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if grid[ny][nx] >= 1:
                    cnt += 1

        # 높이 증가
        grid[cy][cx] += cnt

    # 특수 영양제 사라짐
    special = []

    # 해당 년도에 특수 영양제를 맞은 땅을 제외하고
    # 높이가 2이상인 리브로수를 높이 2만큼 잘라내고
    # 해당 땅에 특수 영양제 올려주기
    for y in range(N):
        for x in range(N):
            if grid[y][x] >= 2:
                if not v[y][x]:
                    grid[y][x] -= 2
                    special.append([y, x])


# 높이 총합 출력
print(sum(sum(row) for row in grid))
