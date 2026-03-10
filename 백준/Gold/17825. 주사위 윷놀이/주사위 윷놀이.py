# 좌충수 금지
# 오타 금지

# 구현 플랜
# [1] product 사용, 구현 처럼 풀기 -> 2번보다 쉬우나... 비효율적이다 2번해보고 안되면 1번하자
# [2] 백트래킹으로 풀기

# 말 4개
# 빨간색 선으로 만 이동
# 파란색 원에서 시작시 파란색 선으로 가야 함
# 도착칸으로 이동한 경우 주사위에 나온 수와 관계 없이 이동 마치기
# 10개의 턴으로 이루어진다.
# 도착칸에 있지 않은 말을 하나 골라 주사위에 나온 수 만큼 이동
# 이때 이동을 마치는 칸에 다른 말이 있으면 그말은 고를 수 없음
# 단 이동을 마치는 칸이 도착칸이면 고를 수 있음.
# 말이 이동을 마칠때마다 점수 추가

# [백트래킹 필요요소]
# 1) 현재 이동할 depth 번째 주사위 수
# 2) 어떤 말을 선택할지 idx, s_num
# 2-1) 선택할 때 이동 가능한 말이여야 함
# 3) s_num에 따른 사용할 길 선택

road = [
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, -1],
    [0, 2, 4, 6, 8, 10, 13, 16, 19, 25, 30, 35, 40, -1],
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30, 35, 40, -1],
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 27, 26, 25, 30, 35, 40, -1]
]


def dfs(depth, sm):
    global ans

    # 남은 기회 40으로 꽉꽉채워도 안된다면
    if sm + (10 - depth) * 40 <= ans:
        return

    # 종료 조건
    if depth == 10:
        ans = max(ans, sm)
        return

    # 현재 주사위 수
    step = dices[depth]

    # 어떤 말을 선택할지
    for i in range(4):
        mal_idx = i
        dol_idx, road_idx = dol[mal_idx]
        dol_num = road[road_idx][dol_idx]

        nxt_road_idx = road_idx

        # 도착칸에 있으면 선택안함
        if dol_num == -1:
            continue

        # 전진
        nxt_dol_idx = dol_idx + step

        # 인덱스 초과 처리
        if road_idx == 0:
            nxt_dol_idx = min(21, nxt_dol_idx)

            # 0번 길일 경우 분기 처리
            if nxt_dol_idx == 5:
                nxt_road_idx = 1

            elif nxt_dol_idx == 10:
                nxt_road_idx = 2

            elif nxt_dol_idx == 15:
                nxt_road_idx = 3

        elif road_idx == 1:
            nxt_dol_idx = min(13, nxt_dol_idx)

        elif road_idx == 2:
            nxt_dol_idx = min(17, nxt_dol_idx)

        elif road_idx == 3:
            nxt_dol_idx = min(23, nxt_dol_idx)

        if not can_go(mal_idx, nxt_dol_idx, nxt_road_idx):
            continue

        # 이동
        dol[mal_idx] = [nxt_dol_idx, nxt_road_idx]
        now_add = road[road_idx][nxt_dol_idx]

        if now_add != -1:
            dfs(depth + 1, sm + now_add)

        else:
            dfs(depth + 1, sm)

        # 복원
        dol[mal_idx] = [dol_idx, road_idx]


def can_go(mal_idx, dol_idx, road_idx):
    """현재 돌 상태로 이 움직임을 할 수 있는가"""
    dol_num = road[road_idx][dol_idx]

    # 이동을 마치는 칸이 도착칸이면 고를 수 있음.
    if dol_num == -1:
        return True

    for i in range(4):
        # 자기 자신 제외
        if i == mal_idx:
            continue

        now_dol_idx, now_road_idx = dol[i]

        if now_road_idx == road_idx:
            if now_dol_idx == dol_idx:
                return False

        elif dol_idx <= 5:
            if now_dol_idx == dol_idx:
                return False

        elif road_idx == 0:
            if dol_idx == 20:  # 40
                if now_road_idx == 2 and now_dol_idx == 16:
                    return False
                elif now_road_idx == 3 and now_dol_idx == 22:
                    return False
                elif now_road_idx == 1 and now_dol_idx == 12:
                    return False

            elif now_road_idx == 1:
                continue

            elif now_road_idx == 2:
                if now_dol_idx <= 10:
                    if dol_idx == now_dol_idx:
                        return False

            elif now_road_idx == 3:
                if now_dol_idx <= 15:
                    if dol_idx == now_dol_idx:
                        return False

        elif road_idx == 1:
            if dol_idx == 9:  # 25번 노드
                if now_road_idx == 2 and now_dol_idx == 13:
                    return False
                elif now_road_idx == 3 and now_dol_idx == 19:
                    return False
            elif dol_idx == 10:  # 30
                if now_road_idx == 2 and now_dol_idx == 14:
                    return False
                elif now_road_idx == 3 and now_dol_idx == 20:
                    return False
            elif dol_idx == 11:  # 35
                if now_road_idx == 2 and now_dol_idx == 15:
                    return False
                elif now_road_idx == 3 and now_dol_idx == 21:
                    return False
            elif dol_idx == 12:  # 40
                if now_road_idx == 2 and now_dol_idx == 16:
                    return False
                elif now_road_idx == 3 and now_dol_idx == 22:
                    return False
                elif now_road_idx == 0 and now_dol_idx == 20:
                    return False

        elif road_idx == 2:
            if dol_idx == 13:  # 25번 노드
                if now_road_idx == 1 and now_dol_idx == 9:
                    return False
                elif now_road_idx == 3 and now_dol_idx == 19:
                    return False
            elif dol_idx == 14:  # 30
                if now_road_idx == 1 and now_dol_idx == 10:
                    return False
                elif now_road_idx == 3 and now_dol_idx == 20:
                    return False
            elif dol_idx == 15:  # 35
                if now_road_idx == 1 and now_dol_idx == 11:
                    return False
                elif now_road_idx == 3 and now_dol_idx == 21:
                    return False
            elif dol_idx == 16:  # 40
                if now_road_idx == 1 and now_dol_idx == 12:
                    return False
                elif now_road_idx == 3 and now_dol_idx == 22:
                    return False
                elif now_road_idx == 0 and now_dol_idx == 20:
                    return False

        elif road_idx == 3:
            if dol_idx == 19:  # 25번 노드
                if now_road_idx == 1 and now_dol_idx == 9:
                    return False
                elif now_road_idx == 2 and now_dol_idx == 13:
                    return False
            elif dol_idx == 20:  # 30
                if now_road_idx == 1 and now_dol_idx == 10:
                    return False
                elif now_road_idx == 2 and now_dol_idx == 14:
                    return False
            elif dol_idx == 21:  # 35
                if now_road_idx == 1 and now_dol_idx == 11:
                    return False
                elif now_road_idx == 2 and now_dol_idx == 15:
                    return False
            elif dol_idx == 22:  # 40
                if now_road_idx == 1 and now_dol_idx == 12:
                    return False
                elif now_road_idx == 2 and now_dol_idx == 16:
                    return False
                elif now_road_idx == 0 and now_dol_idx == 20:
                    return False

    return True


########################################
dices = list(map(int, input().split()))
########################################
# (현재위치(idx) / 사용하는 도로)
dol = [[0, 0], [0, 0], [0, 0], [0, 0]]
ans = 0
dfs(0, 0)

print(ans)
