n = int(input())
lst = [int(input()) for _ in range(n)]

for i in range(n-1):
    for j in range(n - i - 1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for k in lst:
    print(k)
