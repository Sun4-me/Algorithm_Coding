import sys
score = [int(sys.stdin.readline()) for _ in range(10)]
total = 0

for i in score:
    total += i
    if total >= 100:
        if total - 100 > 100 - (total - i):
            total -= i
        break
print(total)
