t = int(input())


def fac(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num


def nCr(n, r):
    return fac(n) // (fac(r) * fac(n - r))


for _ in range(t):
    n, m = map(int, input().split())
    print(nCr(m, n))
