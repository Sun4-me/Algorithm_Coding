def fac(n):
    if n == 0:
        return 1
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


print(fac(int(input())))
