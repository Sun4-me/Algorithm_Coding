################
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
################
# 가능한 최솟값의 집합
possible_cnt = []

# 전체 보드에서 가능한 영역 탐색
for i in range(n - 7):
    for j in range(m - 7):
        w = 0  # 시작이 w
        b = 0  # 시작이 b

        # 8 x 8 격자 내 탐색
        for row in range(i, i + 8):
            for col in range(j, j + 8):
                if (row + col) % 2 == 0:
                    if board[row][col] != "W":
                        w += 1  # 시작점 w일때
                    else:
                        b += 1  # 시작점 b일때
                else:
                    if board[row][col] != "B":
                        w += 1
                    else:
                        b += 1

        possible_cnt.append(min(w, b))

print(min(possible_cnt))
