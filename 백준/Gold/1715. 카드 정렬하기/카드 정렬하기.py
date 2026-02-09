from heapq import heappush, heappop, heapify

n = int(input())
cards = [int(input()) for _ in range(n)]
heapify(cards)

ans = 0

# 인덱스 주의
while len(cards) >= 2:
    a = heappop(cards)
    b = heappop(cards)

    ans += a + b

    heappush(cards, a+b)

print(ans)
