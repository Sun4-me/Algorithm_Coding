n, m = map(int, input().split())


box = []

for i in range(n):
    box.append(i + 1)

for _ in range(m):
    i, j = map(int, input().split())
    box[i - 1], box[j - 1] = box[j - 1], box[i - 1]

for i in range(n):
    print(box[i], end=" ")
