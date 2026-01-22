lst = [int(input()) for _ in range(9)]

res = sum(lst)

fake1, fake2 = 0, 0

for i in range(9):
    for j in range(i + 1, 9):
        if res - lst[i] - lst[j] == 100:
            fake1, fake2 = lst[i], lst[j]
            break

lst.remove(fake1)
lst.remove(fake2)
lst.sort()

for i in lst:
    print(i)
