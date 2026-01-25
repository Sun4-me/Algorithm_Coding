n = int(input())
num = n
cnt = 0

while True:
    cnt += 1

    left = num // 10
    right = num % 10

    total = left + right

    num = (right * 10) + (total % 10)

    if num == n:
        break

print(cnt)
