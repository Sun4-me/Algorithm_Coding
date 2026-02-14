def recur(n, start, end, middle):
    if n == 1:
        print(start, end)
        return

    recur(n - 1, start, middle, end)
    print(start, end)
    recur(n - 1, middle, end, start)


n = int(input())

print(2 ** n - 1)
recur(n, 1, 3, 2)
