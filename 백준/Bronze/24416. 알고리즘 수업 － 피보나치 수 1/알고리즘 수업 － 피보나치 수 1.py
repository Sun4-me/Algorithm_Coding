def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    global cnt2
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        cnt2 += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

n = int(input())
f = [0] * (n + 1)
cnt1 = cnt2 = 0

cnt1 = fibonacci(n)

print(cnt1, cnt2)