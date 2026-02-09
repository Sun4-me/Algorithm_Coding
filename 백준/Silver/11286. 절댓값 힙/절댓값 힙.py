from heapq import heappush, heappop, heapify

n = int(input())
command = [int(input()) for _ in range(n)]
hq = []
heapify(hq)

for num in command:
    if num == 0:
        if hq:
            t = heappop(hq)
            print(t[0] * t[1])
        else:
            # 비어있는 경우
            print(0)
    else:
        if num > 0:
            heappush(hq, (num, 1))
        else:
            heappush(hq, (-num, -1))