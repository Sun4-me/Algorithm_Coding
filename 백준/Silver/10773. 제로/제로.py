import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
queue = deque()

for i in range(k):
    num = int(input())
    if num == 0:
        queue.pop()

    else:
        queue.append(num)

print(sum(queue))
