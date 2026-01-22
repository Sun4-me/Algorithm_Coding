import sys

input = sys.stdin.readline
a, b = map(int, input().split())
c = int(input())

hour = c // 60
minute = c % 60

while True:
    if hour == minute == 0:
        break

    if minute != 0:
        if b + minute >= 60:
            b = (b + minute) % 60
            a += 1
            if a == 24:
                a = 0

        else:
            b += minute

        minute = 0

    else:
        a += 1
        if a == 24:
            a = 0
        hour -= 1


print(a, b)