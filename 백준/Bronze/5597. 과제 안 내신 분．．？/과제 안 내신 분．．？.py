import sys

input = sys.stdin.readline
lst = [int(input()) for _ in range(28)]
res = []

for i in range(1, 31):
    if i not in lst:
        res.append(i)

res.sort()
print(res[0])
print(res[1])
