a = []
max = 0

for _ in range(9):
    row = list(map(int, input().split()))
    a.append(row)
    for i in row:
        if i > max:
            max = i


for row in range(9):
    for col in range(9):
        if a[row][col] == max:
            print(max)
            print(row + 1, col + 1)
