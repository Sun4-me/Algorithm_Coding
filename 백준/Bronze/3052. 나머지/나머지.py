res = []

for i in range(10):
    a = int(input())

    if a % 42 not in res:
        res.append(a % 42)

print(len(res))
