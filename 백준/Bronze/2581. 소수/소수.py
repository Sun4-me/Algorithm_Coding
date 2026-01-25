m = int(input())
n = int(input())

total = 0
min_num = 0

for i in range(n, m - 1, -1):
    if i == 1:
        break
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        total += i
        min_num = i

if total > 0:
    print(total)
    print(min_num)

else:
    print(-1)
