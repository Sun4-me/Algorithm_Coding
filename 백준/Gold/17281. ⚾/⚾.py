from itertools import permutations
import sys

input = sys.stdin.readline
##########################################################
N = int(input().strip())
log = [list(map(int, input().split())) for _ in range(N)]
##########################################################
max_score = 0

for per in permutations(range(1, 9)):
    taza = list([*per[:3], 0, *per[3:]])
    total_score = 0
    idx = 0

    for k in range(N):

        # 가지치기
        if total_score + (N - k) * 24 < max_score:
            break

        now_score = 0  # 현재 이닝 점수
        out_count = 0  # 현재 아웃 카운트
        zooza_0, zooza_1, zooza_2 = 0, 0, 0  # 주자 상황

        while True:
            if out_count == 3:
                break

            now_taza = taza[idx]

            case = log[k][now_taza]

            if case == 1:  # 안타

                if zooza_2 == 1:
                    zooza_2 = 0
                    now_score += 1

                if zooza_1 == 1:
                    zooza_1 = 0
                    zooza_2 = 1

                if zooza_0 == 1:
                    zooza_0 = 0
                    zooza_1 = 1

                zooza_0 = 1


            elif case == 2:  # 2루타

                if zooza_2 == 1:
                    zooza_2 = 0
                    now_score += 1

                if zooza_1 == 1:
                    zooza_1 = 0
                    now_score += 1

                if zooza_0 == 1:
                    zooza_0 = 0
                    zooza_2 = 1

                zooza_1 = 1

            elif case == 3:  # 3루타

                now_score += zooza_0 + zooza_1 + zooza_2

                zooza_0 = 0
                zooza_1 = 0
                zooza_2 = 0

                zooza_2 = 1

            elif case == 4:  # 홈런

                now_score += zooza_0 + zooza_1 + zooza_2 + 1

                zooza_0 = 0
                zooza_1 = 0
                zooza_2 = 0

            elif case == 0:  # 아웃
                out_count += 1

            idx = (idx + 1) % 9

        total_score += now_score

    max_score = max(max_score, total_score)

print(max_score)
