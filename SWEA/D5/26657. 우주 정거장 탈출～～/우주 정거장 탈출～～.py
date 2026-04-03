from collections import deque

# 우주선 자발적 이동 우선순위: 하, 우, 상, 좌
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


# ===========================================================
def inb(y, x):
    """격자 범위 내 확인"""
    return 0 <= y < N and 0 <= x < M


def how_dist(y1, x1, y2, x2):
    """맨해튼 거리"""
    return abs(y1 - y2) + abs(x1 - x2)


# ===========================================================
def draw_hole():
    """블랙 / 화이트 홀 그리기 및 중심점 저장"""
    global center_set
    center_set = set()  # 중심점 추락 체크를 위한 Set

    for i in range(H):
        color, cy, cx, k = holes_info[i]

        # 입력받은 1-index 좌표를 0-index로 변환
        cy, cx = cy - 1, cx - 1
        holes_info[i][1], holes_info[i][2] = cy, cx
        center_set.add((cy, cx))

        w = k // 2  # 중심점으로부터의 양 끝 거리
        for y in range(cy - w, cy + w + 1):
            for x in range(cx - w, cx + w + 1):
                if not inb(y, x): continue
                if color == 0:  # 블랙홀
                    black[y][x] = (cy, cx)
                elif color == 1:  # 화이트홀
                    white[y][x] = (cy, cx)


# ===========================================================
def make_path():
    """역방향 BFS | 탈출구부터의 모든 최단 거리 계산"""
    path = [[-1] * M for _ in range(N)]
    path[ey][ex] = 0
    q = deque([(ey, ex)])

    while q:
        cy, cx = q.popleft()

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if not inb(ny, nx): continue
            if obstacle[ny][nx] == 1: continue

            # 방문하지 않은 곳만 갱신
            if path[ny][nx] == -1:
                path[ny][nx] = path[cy][cx] + 1
                q.append((ny, nx))

    return path


# ===========================================================
def spaceship_move(step):
    """우주선의 이동 (자발적 이동)"""
    global sy, sx

    for _ in range(step):
        moved = False
        for k in range(4):
            ny, nx = sy + dy[k], sx + dx[k]
            if not inb(ny, nx): continue
            if obstacle[ny][nx] == 1: continue

            # 목적지까지의 거리가 줄어드는 방향(최단 경로)으로만 이동
            if path[ny][nx] != -1 and path[sy][sx] != -1 and path[ny][nx] < path[sy][sx]:
                sy, sx = ny, nx
                moved = True
                break

        # 이동할 수 없으면 남은 관성 스텝 무시
        if not moved:
            break

        # 한 칸 이동할 때마다 즉시 중심점 추락 및 탈출 여부 확인
        if (sy, sx) in center_set:
            return "CRASH"
        if sy == ey and sx == ex:
            return "EXIT"

    return "OK"


# ===========================================================
def move_gravity(cy, cx, color):
    """중력장에 의한 단일 이동 처리"""
    global sy, sx

    # 좌표 차이에 따른 8방향 힘 계산
    dy_dir = 0 if sy == cy else (1 if cy > sy else -1)
    dx_dir = 0 if sx == cx else (1 if cx > sx else -1)

    if color == 0:  # 블랙홀: 중심점을 향해 1칸 당겨짐
        ny, nx = sy + dy_dir, sx + dx_dir
    else:  # 화이트홀: 중심점 반대 방향으로 1칸 밀려남
        ny, nx = sy - dy_dir, sx - dx_dir

    if not inb(ny, nx): return False
    if obstacle[ny][nx] == 1: return False

    sy, sx = ny, nx
    return True


# ===========================================================
def hole_gravity():
    """블랙홀/화이트홀 중력장 우선순위 판단 및 적용"""
    coord = []

    if black[sy][sx] is not None:
        cy, cx = black[sy][sx]
        coord.append((how_dist(sy, sx, cy, cx), 0, (cy, cx)))

    if white[sy][sx] is not None:
        cy, cx = white[sy][sx]
        coord.append((how_dist(sy, sx, cy, cx), 1, (cy, cx)))

    if not coord: return False

    # 1. 맨해튼 거리 오름차순, 2. 블랙홀(0) 우선순위로 정렬
    coord.sort()

    for _, color, (cy, cx) in coord:
        if move_gravity(cy, cx, color):
            return True  # 차선책 탐색 중 하나라도 이동 성공 시 True 반환

    return False  # 모든 겹친 홀의 영향이 쓰레기에 막힌 경우


# ===========================================================
T = int(input())
for case in range(1, T+1):
    # 입력 및 초기화
    N, M = map(int, input().split())
    sy, sx, ey, ex = map(lambda x: int(x) - 1, input().split())
    obstacle = [list(map(int, input().split())) for _ in range(N)]

    black = [[None] * M for _ in range(N)]
    white = [[None] * M for _ in range(N)]

    H = int(input())
    holes_info = [list(map(int, input().split())) for _ in range(H)]

    # ===========================================================
    # 메인 실행부
    path = make_path()
    draw_hole()

    buff = False  # 관성 버프 유무
    result_code = -1  # 초기 상태코드
    result_time = 0

    for t in range(1, 101):
        step = 2 if buff else 1

        # [1]. 우주선의 자발적 이동
        res = spaceship_move(step)
        if res == "CRASH":
            result_code = -2
            result_time = t
            break
        elif res == "EXIT":
            result_code = 1
            result_time = t
            break

        # [2]. 블랙홀/화이트홀 중력장의 적용
        if hole_gravity():
            buff = True  # 중력 이동 성공 시 다음 턴 관성 획득

            # 중력에 의한 강제 이동 직후 추락/탈출 여부 한 번 더 체크
            if (sy, sx) in center_set:
                result_code = -2
                result_time = t
                break
            if sy == ey and sx == ex:
                result_code = 1
                result_time = t
                break
        else:
            buff = False  # 강제 이동 실패 및 해당사항 없을 시 버프 상실

    # 결과 출력
    if result_code == -1:
        print(f"#{case} -1")
    else:
        print(f"#{case} {result_code} {result_time}")