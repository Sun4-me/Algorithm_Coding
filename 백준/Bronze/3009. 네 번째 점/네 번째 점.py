x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

ans_x, ans_y = 0, 0

if x1 == x2:
    ans_x = x3

elif x1 == x3:
    ans_x = x2

else:
    ans_x = x1

if y1 == y2:
    ans_y = y3

elif y1 == y3:
    ans_y = y2

else:
    ans_y = y1

print(ans_x, ans_y)
