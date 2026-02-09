# 모든 사람이 기다리지 않아도 되는 컴퓨터의 최소 개수 구하기
# 각 자리를 이용한 사람 수 구하기
# 가장 번호가 작은 자리에 앚아야 함
from heapq import heappush, heappop, heapify
import sys

input = sys.stdin.readline

n = int(input())
hq = []
heapify(hq)

for _ in range(n):
    p, q = map(int, input().split())
    heappush(hq, (p, q))

total_pc = 1  # 총 pc 수
res = [1]
k = heappop(hq)

pc_time = [k[1]]
min_num = k[1]
while hq:
    t = heappop(hq)

    if t[0] < min_num:
        min_num = min(min_num, t[1])
        res.append(1)
        pc_time.append(t[1])
        total_pc += 1

    elif t[0] > min_num:
        # 번호 중에 제일 작은애랑 교체
        for i in range(total_pc):
            if t[0] > pc_time[i]:
                pc_time[i] = t[1]
                res[i] += 1
                min_num = min(pc_time)
                break

print(total_pc)
print(*res)
