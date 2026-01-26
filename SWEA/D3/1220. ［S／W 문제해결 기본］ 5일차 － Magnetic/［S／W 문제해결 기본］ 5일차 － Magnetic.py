# 세로만 확인
# 1개 만있을 경우 체크 안해도 됨
# 1: N : 아래로, 2: S : 위로
for case in range(1, 11):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for row in range(n):
        state = False
        for col in range(n):
            if grid[col][row] == 1:
                state = True

            elif state and grid[col][row] == 2:
                state = False
                cnt += 1

    print(f"#{case} {cnt}")
