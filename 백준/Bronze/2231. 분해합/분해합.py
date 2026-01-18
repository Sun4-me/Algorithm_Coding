n = int(input())
res = 0
for i in range(n):
    a = list(map(int, str(i)))
    if n == sum(a) + i:
        res = i
        break
print(res)
