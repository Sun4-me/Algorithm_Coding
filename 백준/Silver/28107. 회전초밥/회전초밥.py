# n명의 손님 m개의 초밥
# 1부터 n까지 순서대로 초밥받음
# 초밥을 먹으면 뒷 번호들은 해당 초밥 못먹음
# 아무도 안먹으면 버려짐
# 먹고 싶은 초밥이면 반드시 먹음
# 목록에 안적혀있으면 반드시 먹지 않음
# 각 종류의 초밥은 최대 한번만 먹ㅇ음
# 각 손님이 먹게 되는 초밥개수 구하기
from heapq import heappush, heappop, heapify
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

hq = []
heapify(hq)

# (번호가 작은거 and 초밥 종류) 기준으로 최소힙
for i in range(1, n + 1):
    sushi = list(map(int, input().split()))
    for j in range(1, sushi[0] + 1):
        heappush(hq, (i, sushi[j]))

# 스시 종류 및 순서
sushi = list(map(int, input().split()))
sushi_set = [0] * 200_001
for i in range(m):
    sushi_set[sushi[i]] += 1

res = [0] * (n + 1)
# 주문 목록에 적힌 초밥 종류가 모두 다르니
# 초밥당 한번 먹는거 보장됨
# 초밥당 번호가 가장 작은 사람이 한번 먹고 무조건 끝남
for i in range(len(hq)):
    t = heappop(hq)

    if sushi_set[t[1]]:
        sushi_set[t[1]] -= 1
        res[t[0]] += 1

print(*res[1:])
