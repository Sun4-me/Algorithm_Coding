t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    room = (n - 1) // h + 1
    if floor == 0:
        floor = h
    print(floor * 100 + room)
