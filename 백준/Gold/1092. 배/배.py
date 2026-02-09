# 화물을 배에 실어야 함
# 화물은 박스 안에
# 크레인 N대, 1분에 박스 하나씩. 크레인 동시에 움직ㄷ임
# 무게재한 보다 작아야 크레인으로 가능
# 모든 박스 옮기는 시간의 최솟 값 구하기
# 못 옮기면 -1 출력
import sys

# 크레인 n대
n = int(input())
# n대 크레인의 무게 재한
limit = list(map(int, input().split()))
# 박스의 수 m개
m = int(input())
# m개 박스의 무게
weight = list(map(int, input().split()))

limit.sort()
weight.sort()

# 가장 큰 크레인이 가장 큰 무게를 못 옮기면 -1 종료
if limit[-1] < weight[-1]:
    print(-1)
    sys.exit()

min_num = weight[0]

# 시간 관리..
for i in range(n-1, -1, -1):
    if limit[i] < min_num:
        limit.pop(i)

length = len(limit)

v = [0] * m

cnt = 0
time = 0
while True:
    # 박스 다 주웠으면 끝
    if cnt == m:
        break

    for i in range(length):
        flag = False
        idx = 0
        for j in range(m):
            if limit[i] < weight[j]:
                break

            elif v[j] == 0 and limit[i] >= weight[j]:
                flag = True
                idx = j

        if flag:
            v[idx] = 1
            cnt += 1

    time += 1

print(time)
