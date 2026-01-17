N, M = map(int, input().split())

box = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    box[i - 1 : j] = box[i - 1 : j][::-1]

print(*box)
