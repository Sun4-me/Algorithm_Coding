from pprint import *


# 가로 5개 세로 5개 대각선 2개만 체크 하면 됨
def check():
    # 빙고 수
    cnt = 0
    # 가로
    for row in range(5):
        zero_count = 0
        for col in range(5):
            if grid[row][col] == 0:
                zero_count += 1
            else:
                break

        if zero_count == 5:
            cnt += 1

    # 세로
    for col in range(5):
        zero_count = 0
        for row in range(5):
            if grid[row][col] == 0:
                zero_count += 1
            else:
                break

        if zero_count == 5:
            cnt += 1

    # (0,0) 오른쪽 아래대각선
    dy, dx = 1, 1
    cy, cx = 0, 0
    zero_count = 1
    if grid[cy][cx] == 0:
        while True:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < 5 and 0 <= nx < 5:
                if grid[ny][nx] == 0:
                    zero_count += 1
                    cy, cx = ny, nx
                else:
                    break
            else:
                break

    if zero_count == 5:
        cnt += 1

    # (4,0) 오른쪽 위 대각선
    dy, dx = -1, 1
    cy, cx = 4, 0
    zero_count = 1
    if grid[cy][cx] == 0:
        while True:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < 5 and 0 <= nx < 5:
                if grid[ny][nx] == 0:
                    zero_count += 1
                    cy, cx = ny, nx
                else:
                    break
            else:
                break

    if zero_count == 5:
        cnt += 1

    return cnt


##############################################################
grid = [list(map(int, input().split())) for _ in range(5)]
order = []
for _ in range(5):
    tmp = list(map(int, input().split()))
    order.extend(tmp)
##############################################################
# 가장 적은 수로 빙고 3개 만드는 방법은 12번임
# 11번 주문까지는 0으로 처리 해주자
for row in range(5):
    for col in range(5):
        if grid[row][col] in order[:11]:
            grid[row][col] = 0

ans_cnt = 11
real_order = order[11:].copy()
while True:
    target = real_order.pop(0)
    for row in range(5):
        for col in range(5):
            if grid[row][col] == target:
                grid[row][col] = 0
                ans_cnt += 1
                cnt = check()
                if cnt >= 3:
                    print(ans_cnt)
                    quit()
