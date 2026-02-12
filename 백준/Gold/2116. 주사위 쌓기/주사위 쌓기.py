# 문제를 잘 읽자 !
# 6개 경우의 수 다 해보고
# 각각 최대치 중에 제일 최대치 구하면 끝.
from pprint import *

# A B C D E F
# 윗면  사이드 사이드 사이드 사이드 뒷면

# 반대면 쌍
# A:F, B:D, C:E
# 0:5, 1:3, 2:4
reverse_dict = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]

res = 0

for i in range(6):
    # 1번 주사위 처리
    now_top = dices[0][i]
    now_total = 0

    top_idx = i
    bottom_idx = reverse_dict[i]
    now_bottom = dices[0][bottom_idx]

    now_dice = set(dices[0])

    now_dice.remove(now_bottom)
    now_dice.remove(now_top)

    one_dice_max = max(now_dice)
    now_total += one_dice_max
    # 1부터 n주사위 처리
    for j in range(1, n):
        for k in range(6):
            if dices[j][k] == now_top:
                bottom_idx = k
                now_bottom = dices[j][bottom_idx]

                top_idx = reverse_dict[k]
                now_top = dices[j][top_idx]
                break

        now_dice = set(dices[j])

        now_dice.remove(now_bottom)
        now_dice.remove(now_top)

        one_dice_max = max(now_dice)
        now_total += one_dice_max

    res = max(res, now_total)

print(res)
