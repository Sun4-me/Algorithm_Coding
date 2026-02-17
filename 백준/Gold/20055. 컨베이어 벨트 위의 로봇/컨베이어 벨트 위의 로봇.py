from collections import deque

###########################################
n, k = map(int, input().split())
belt = deque()
lines = list(map(int, input().split()))

for i in range(2 * n):
    belt.append(lines[i])
###########################################
robots = deque([0 for _ in range(n)])

step = 0

while True:
    step += 1

    belt.rotate(1)
    robots.rotate(1)

    robots[n - 1] = 0

    for i in range(n - 1, 0, -1):
        if robots[i - 1] == 1:
            if belt[i] >= 1 and robots[i] == 0:
                robots[i - 1] = 0
                robots[i] = 1
                belt[i] -= 1

    robots[n - 1] = 0

    if belt[0] >= 1:
        belt[0] -= 1
        robots[0] = 1

    if belt.count(0) >= k:
        break

print(step)
