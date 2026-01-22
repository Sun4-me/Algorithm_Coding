a = int(input())  # 원래 온도
b = int(input())  # 목표 온도
c = int(input())  # (얼어있음) 1도 데우는데 걸리는시간
d = int(input())  # (얼어있음) 해동하는데 걸리는 시간
e = int(input())  # (안얼음) 1도 데우는데 걸리는 시간

cnt = 0
flag = True  # 얼음

while True:
    if a == b:
        break

    if a < 0 and flag:
        a += 1
        cnt += c

    elif a == 0 and flag:
        cnt += d
        flag = False

    else:
        a += 1
        cnt += e

print(cnt)
