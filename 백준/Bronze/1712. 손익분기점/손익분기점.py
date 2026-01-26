a, b, c = map(int, input().split())
# a 고정 b 가변 | c 가격

if b >= c:
    print(-1)
else:
    print(int(a / (c - b) + 1))
