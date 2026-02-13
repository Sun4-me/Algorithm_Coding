# from pprint import *

def swap(a, b):
    tmp = line[b]
    line[b] = line[a]
    line[a] = tmp
    return


# 만난 순간 1초에 한번씩 뛰어 넘음
# 자신 앞에 반대 방향으로 움직이던 개미가 있을 경우에만 점프
###################################################
n1, n2 = map(int, input().split())
go_right = list(input())
go_right = go_right[::-1]
go_left = list(input())
t = int(input())
###################################################
# 왼쪽이동 -1 오른쪽 이동 1
for i in range(n1):
    go_right[i] = (go_right[i], 1)

for i in range(n2):
    go_left[i] = (go_left[i], -1)

line = go_right + go_left

while True:
    if t == 0:
        break

    swap_lst = []

    for i in range(n1 + n2 - 1):
        if line[i][1] == 1 and line[i + 1][1] == -1:
            swap_lst.append((i, i + 1))

    for a, b in swap_lst:
        swap(a, b)

    t -= 1

for i in range(n1 + n2):
    print(line[i][0], end="")
