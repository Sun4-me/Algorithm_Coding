from collections import defaultdict

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for case in range(1, T+1):
    # 셀의 개수, 격리시간, 미생물 군집의 개수
    N, M, K = map(int, input().split())
    micro = defaultdict(list)
    for _ in range(K):
        # 세로, 가로, 미생물 수, 이동방향
        y, x, cnt, d = map(int, input().split())
        micro[(y, x)].append((cnt, d - 1))

    while M:
        nxt_micro = defaultdict(list)

        # 이동
        for key, val in micro.items():
            cy, cx = key
            cnt, k = val[0]

            ny, nx = cy + dy[k], cx + dx[k]
            if ny == 0 or ny == N - 1 or nx == 0 or nx == N - 1:
                k ^= 1
                cnt //= 2

            nxt_micro[(ny, nx)].append((cnt, k))

        # 이동 후 처리
        for key, val in nxt_micro.items():
            length = len(val)

            if length != 1:
                val.sort(reverse=True)
                change_direct = val[0][1]
                total = 0
                for i in range(length):
                    total += val[i][0]

                nxt_micro[key] = [(total, change_direct)]

        micro = nxt_micro
        M -= 1

    ans = 0
    for val in micro.values():
        ans += val[0][0]

    print(f"#{case} {ans}")