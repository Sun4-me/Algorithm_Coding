import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

queue = deque()

for _ in range(n):
    command = list(map(int, input().split()))

    if command[0] == 1:
        queue.appendleft(command[1])

    elif command[0] == 2:
        queue.append(command[1])

    elif command[0] == 3:
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif command[0] == 4:
        if queue:
            print(queue.pop())
        else:
            print(-1)

    elif command[0] == 5:
        print(len(queue))

    elif command[0] == 6:
        if queue:
            print(0)
        else:
            print(1)

    elif command[0] == 7:
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif command[0] == 8:
        if queue:
            print(queue[-1])
        else:
            print(-1)
