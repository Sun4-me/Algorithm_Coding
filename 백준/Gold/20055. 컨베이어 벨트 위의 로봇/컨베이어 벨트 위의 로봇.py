from collections import deque

#############################################
n, k = map(int, input().split())
walk = deque(map(int, input().split()))
people = deque(0 for _ in range(2 * n))
#############################################
zero_cnt = 0 # 안정성 0의 갯수
time = 0 # 실험 횟수

while True:
    if zero_cnt >= k:
        break

    # 1) 무빙 워크 한 칸 회전, 사람도 같이 회전함
    walk.rotate(1)
    people.rotate(1)

    # n번 칸 위치에 사람이 있다면 내리기
    if people[n - 1] == 1:
        people[n - 1] = 0

    # 2) 먼저 있는 사람 부터 움직이기
    for i in range(n - 2, -1, -1):
        # 사람이 있다면
        if people[i] == 1:
            # 다음 갈 곳에 사람이 없고 다음 갈 곳에 안정성이 0이 아니라면
            if people[i + 1] == 0 and walk[i + 1] > 0:
                # 이동
                people[i + 1] = 1
                people[i] = 0
                # 안정성 - 1
                walk[i + 1] -= 1
                # 안정성 0이되면 체크
                if walk[i + 1] == 0:
                    zero_cnt += 1

    # n번 칸 위치에 사람이 있다면 내리기
    if people[n - 1] == 1:
        people[n - 1] = 0

    # 3) 1번 칸에 사람이 없고 안정성이 0이 아니라면 올리기
    if people[0] == 0 and walk[0] > 0:
        people[0] = 1
        walk[0] -= 1
        # 안정성 0이되면 체크
        if walk[0] == 0:
            zero_cnt += 1

    time += 1

print(time)
