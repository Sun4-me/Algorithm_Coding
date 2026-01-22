n = int(input())
lst = [float(input()) for _ in range(n)]

for i in range(1, n):
    lst[i] = max(lst[i], lst[i] * lst[i - 1])

print(f'{max(lst):.3f}')
