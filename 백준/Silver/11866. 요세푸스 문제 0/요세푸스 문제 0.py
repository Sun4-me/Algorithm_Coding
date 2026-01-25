n, k = map(int, input().split())
lst = [i for i in range(1, n + 1)]
res = []
offset = k - 1
while True:

    res.append(lst.pop(offset))
    offset += k - 1

    if not lst:
        break

    if offset >= len(lst):
        offset = offset % len(lst)

print("<", end="")
print(*res, end="", sep=', ')
print(">", end="")
