import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    lst = list(map(int, input().split()))
    case = lst.pop(0)
    cnt = 0
    len_lst = len(lst)
    for i in range(len_lst - 1):
        for j in range(len_lst - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                cnt += 1

    print(case, cnt)