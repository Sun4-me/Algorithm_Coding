piece = list(map(int, input().split()))

correct_lst = [1, 1, 2, 2, 2, 8]
res = []

for i in range(6):
    res.append(correct_lst[i] - piece[i])

print(*res)