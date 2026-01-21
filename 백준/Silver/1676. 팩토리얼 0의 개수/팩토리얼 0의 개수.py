n = int(input())


def fac(k):
    res = 1
    for i in range(2, k + 1):
        res *= i
    return res


tmp = str(fac(n))[::-1]
cnt = 0

for i in tmp:
    if int(i) != 0:
        break
    cnt += 1

print(cnt)
