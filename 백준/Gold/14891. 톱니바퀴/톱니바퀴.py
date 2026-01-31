# 톱니 바퀴 4개
# 1, 2, 3, 4
# 톱니바퀴 한칸씩 총 k번회전
# 시계 or 반시계
# 맞닿은 극이 다르다면, 회전한 방향과 반대방향으로 회전
from collections import deque

topnis = [deque(list((map(int, input())))) for _ in range(4)]
# 회전 시킨 방법의 수
k = int(input())
# 방법들
# 회전 시킨 톱니의 번호 | 방향 1이면 시계, -1 이면 반시계
nodes = [list(map(int, input().split())) for _ in range(k)]


def bingle(num, direct):
    num = num - 1
    if direct == 1:  # 시계 방향
        topnis[num].appendleft(topnis[num].pop())
    else:  # 반시계 방향
        topnis[num].append(topnis[num].popleft())


def check(left, right):
    if topnis[left - 1][2] == topnis[right - 1][6]:
        return False
    else:
        return True


for i in nodes:
    num, direct = i[0], i[1]
    diret_reverse = -1 if direct == 1 else 1
    if num == 1:
        topni_12 = check(1, 2)
        topni_23 = check(2, 3)
        topni_34 = check(3, 4)

        if topni_12:
            bingle(2, diret_reverse)

        if topni_12 and topni_23:
            bingle(3, direct)

        if topni_12 and topni_23 and topni_34:
            bingle(4, diret_reverse)

        bingle(1, direct)

    elif num == 2:
        topni_12 = check(1, 2)
        topni_23 = check(2, 3)
        topni_34 = check(3, 4)

        if topni_12:
            bingle(1, diret_reverse)

        if topni_23:
            bingle(3, diret_reverse)

        if topni_23 and topni_34:
            bingle(4, direct)

        bingle(2, direct)

    elif num == 3:
        topni_12 = check(1, 2)
        topni_23 = check(2, 3)
        topni_34 = check(3, 4)

        if topni_23 and topni_12:
            bingle(1, direct)

        if topni_23:
            bingle(2, diret_reverse)

        if topni_34:
            bingle(4, diret_reverse)

        bingle(3, direct)

    elif num == 4:
        topni_12 = check(1, 2)
        topni_23 = check(2, 3)
        topni_34 = check(3, 4)

        if topni_12 and topni_23 and topni_34:
            bingle(1, diret_reverse)

        if topni_23 and topni_34:
            bingle(2, direct)

        if topni_34:
            bingle(3, diret_reverse)

        bingle(4, direct)

##############################################
# 점수 계산
ans = 0
for i in range(4):
    if topnis[i][0] == 1:
        if i == 0:
            ans += 1
        elif i == 1:
            ans += 2
        elif i == 2:
            ans += 4
        else:
            ans += 8

print(ans)
