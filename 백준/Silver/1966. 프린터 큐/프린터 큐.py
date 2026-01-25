import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    weight = deque(list(map(int, input().split())))
    target_idx = m

    cnt = 0

    while True:
        if len(weight) == 0:
            break

        flag = False
        for i in range(1, len(weight)):
            if weight[i] > weight[0]:
                flag = True
                weight.append(weight.popleft())
                if target_idx == 0:
                    target_idx = len(weight) - 1
                else:
                    target_idx -= 1
                break

        if not flag:
            cnt += 1
            if target_idx == 0:
                break
            target_idx -= 1
            del weight[0]

    print(cnt)
