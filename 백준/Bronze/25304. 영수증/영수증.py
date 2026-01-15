x = int(input())
n = int(input())
c = 0

for _ in range(n):
    a, b = map(int, input().split())
    c += a * b

if x == c:
    print("Yes")
else:
    print("No")
