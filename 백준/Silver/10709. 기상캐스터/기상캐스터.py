h, w = map(int, input().split())
cloudes = [list(input()) for _ in range(h)]

for row in cloudes:
    time = 0
    for i in range(w):
        if row[i] == 'c':
            row[i] = 0
            time = 1

        else:
            if time != 0:
                row[i] = time
                time += 1
            else:
                row[i] = -1

for row in cloudes:
    print(*row)
