from collections import deque

################################################
dx = [0, 0, -1, 1]  # 상 하 좌 우
dy = [-1, 1, 0, 0]


def bfs(x, y):
    v = [0] * n  # 편의점 방문 기록
    q = deque([(x, y)])

    while q:

        cur_x, cur_y = q.popleft()
        if abs(cur_x - target_x) + abs(cur_y - target_y) <= 1000:
            return "happy"

        for i in range(n):
            if v[i] == 0:
                if abs(cur_x - stores[i][0]) + abs(cur_y - stores[i][1]) <= 1000:
                    v[i] = 1
                    q.append(stores[i])

    return "sad"


################################################
# 출발 상근이네 집, 맥주 한박스, 맥주 20개
# 50미터에 한 병씩 마심
# 50미터 가려면 직전에 맥주 한병 마셔야 함
# 편의점에서 맥주 병 버리고 살 수 있는데 20개 넘기면 안됨
# 편의점 나와서도 50미터 가려면 맥주 한병 마셔야 함
# 갈 수 있는 지 없는 지만 알면 됨 !
t = int(input())
for case in range(t):
    n = int(input())
    # 집, 편의점, 페스티벌 좌표
    house_x, house_y = map(int, input().split())
    # set, tuple로 관리
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    target_x, target_y = map(int, input().split())
    ################################################
    res = bfs(house_x, house_y)
    print(res)
