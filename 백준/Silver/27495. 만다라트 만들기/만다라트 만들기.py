grid = [input().split() for _ in range(9)]
case = [[] for _ in range(10)]

k = 1
for y_offset in range(0, 9, 3):
    for x_offset in range(0, 9, 3):
        for row in grid[y_offset:y_offset + 3]:
            case[k].extend(row[x_offset:x_offset + 3])
        k += 1

res = []
for k in range(1, 10):
    if k == 5:
        continue
    mid_goal = case[k][4]
    details = case[k][:4] + case[k][5:]
    details.sort()

    res.append((mid_goal, details))
res.sort()

for mid, dets in res:
    print(f"#{res.index((mid, dets)) + 1}. {mid}")
    for i, det in enumerate(dets):
        print(f"#{res.index((mid, dets)) + 1}-{i + 1}. {det}")

