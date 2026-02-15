import sys
from collections import deque

# 한번 돌려서 풀라면 반드시 두면이 같아야 함

# 특정 두면의 색깔이 일치 한다면.
# 두면을 공유하지 않는 면의 2리스트 각각 양방향 2회
# 두면을 공유하지 않는 경우의 수 3개
# 총 12개 케이스 발생 가능


# 덱 6개로 관리

# 1
# # # 1 2 # # # #
# # # # # # # # #
# 13 # # # # 18 # #
# 15 # # # # 20 # #
# # # # # # # # #
# # # 11 12 # # # #

# 2
# # # # # # # # #
# # # 3 4 # # # #
# # 14 # # 17 # # #
# # 16 # # 19 # # #
# # # 9 10 # # # #
# # # # # # # # #

# 3
# # # # # # # # #
# # # # # # # # #
# 13 14 5 6 17 18 21 22
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

# 4
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# 15 16 7 8 19 20 23 24
# # # # # # # # #
# # # # # # # # #

# 5
# # # 1 # # # # #
# # # 3 # # # # #
# # # 5 # # # # 22
# # # 7 # # # # 24
# # # 9 # # # # #
# # # 11 # # # # #

# 6
# # # # 2 # # # #
# # # # 4 # # # #
# # # # 6 # # 21 #
# # # # 8 # # 23 #
# # # # 10 # # # #
# # # # 12 # # # #
############################################################
index = [
    [  # [1] (2) 5,6,7,8 | (6) 21,22,23,24 같은 색상일 때 검사
        [1, 2, 18, 20, 12, 11, 15, 13],  # 1
        [3, 4, 17, 19, 10, 9, 16, 14]],  # 2

    [  # [2] (1) 1,2,3,4 | (3) 9,10,11,12 같은 색상일 때 검사
        [13, 14, 5, 6, 17, 18, 21, 22],  # 3
        [15, 16, 7, 8, 19, 20, 23, 24]],  # 4

    [  # [3] (4) 13,14,15,16 | (5) 17,18,19,20 같은 색상일 때 검사
        [1, 3, 5, 7, 9, 11, 24, 22],  # 5
        [2, 4, 6, 8, 10, 12, 23, 21]]  # 6
]
############################################################
colors = list(map(int, input().split()))
colors.insert(0, 0)  # 번호 관리 용이용
############################################################
# [0] 주어진 색상의 몇 번면이 같은지 저장
num_colored = [False] * 7

now_side = 0  # 현재 주사위 면
for i in range(1, 22, 4):
    now_side += 1

    flag = True
    color = colors[i]
    for j in range(i + 1, i + 4):
        if colors[j] != color:
            flag = False
            break

    num_colored[now_side] = flag
############################################################
# 돌리고, 각 면이 색상이 같은지 확인
# 반대쪽도 수행
def solve(q1, q2):
    # 오른쪽 회전 검사
    q1.rotate(2)
    if check(q1, q2):
        return True

    # 왼쪽 회전 검사
    q1.rotate(-4)
    if check(q1, q2):
        return True

    q1.rotate(2)  # 복구

    # 오른쪽 회전 검사
    q2.rotate(2)
    if check(q1, q2):
        return True

    # 왼쪽 회전 검사
    q2.rotate(-4)
    if check(q1, q2):
        return True

    return False


def check(q1, q2):
    for i in range(0, 8, 2):
        # 위, 아래 4칸이 모두 같아야 함
        if not (q1[i] == q1[i + 1] == q2[i] == q2[i + 1]):
            return False
    return True


############################################################
q1 = deque()
q2 = deque()

# [1] (2) 5,6,7,8 | (6) 21,22,23,24 같은 색상일 때 검사
if num_colored[2] == num_colored[6] == True:

    for idx in index[0][0]:
        q1.append(colors[idx])
    for idx in index[0][1]:
        q2.append(colors[idx])

    can_solve = solve(q1, q2)

# [2] (1) 1,2,3,4 | (3) 9,10,11,12 같은 색상일 때 검사
elif num_colored[1] == num_colored[3] == True:

    for idx in index[1][0]:
        q1.append(colors[idx])
    for idx in index[1][1]:
        q2.append(colors[idx])

    can_solve = solve(q1, q2)

# [3] (4) 13,14,15,16 | (5) 17,18,19,20 같은 색상일 때 검사
elif num_colored[4] == num_colored[5] == True:

    for idx in index[2][0]:
        q1.append(colors[idx])
    for idx in index[2][1]:
        q2.append(colors[idx])

    can_solve = solve(q1, q2)

# 특정 두면이 같지 않은 경우 애초에 돌려도 불가능
else:
    print(0)
    sys.exit()
############################################################
if can_solve:
    print(1)
else:
    print(0)