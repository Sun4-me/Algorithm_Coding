from itertools import product, combinations


def check(x):
    """현재 열이 합격 기준인가"""
    now_num = grid[0][x]
    cnt = 1

    if K == 1:
        return True

    for y in range(1, D):
        if cnt == 1 and (D - y + 1) < K:
            return False

        if grid[y][x] == now_num:
            cnt += 1

        else:
            now_num = grid[y][x]
            cnt = 1

        if cnt >= K:
            return True

    return False


def change(y, num):
    """약품 사용하기"""
    for x in range(W):
        grid[y][x] = num


T = int(input())
for case in range(1, T + 1):
    D, W, K = map(int, input().split())
    ori_grid = [list(map(int, input().split())) for _ in range(D)]

    min_use = K
    fin = False

    grid = [lst[:] for lst in ori_grid]

    # 사용 횟수
    for use_cnt in range(K):
        if fin:
            break

        # 행 선택
        for rows in combinations(range(D), use_cnt):
            if fin:
                break

            # 약품 선택
            for colors in product((0, 1), repeat=use_cnt):
                for y, color in zip(rows, colors):
                    grid[y] = [color] * W

                for x in range(W):
                    if not check(x):
                        break
                else:
                    min_use = use_cnt
                    fin = True
                    break

                for y in rows:
                    grid[y] = ori_grid[y]

    print(f"#{case} {min_use}")
