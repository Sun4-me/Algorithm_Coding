n = int(input())
square = [1, 1]
for i in range(1, n + 1):
    cnt = len(square) - 1
    for j in range(cnt):
        square.append(1)

side = len(square)
print(side * side)
