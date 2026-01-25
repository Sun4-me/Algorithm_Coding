c = int(input())

for _ in range(c):
    score = list(map(int, input().split()))
    n = score.pop(0)
    average = sum(score) / n
    cnt = 0
    for i in score:
        if i > average:
            cnt += 1

    print("{:.3f}".format((cnt / n) * 100) + "%")
