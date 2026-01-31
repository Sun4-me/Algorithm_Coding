# 상자길이, 공 개수, 시간
l, n, t = map(int, input().split())
balls = []
for _ in range(n):
    line = input().split()
    # 이런거 숫자로 바꿔두고 하자
    direction = 1 if line[1] == "R" else -1
    balls.append([int(line[0]), direction])
#############################################
ans = 0

# 시간이 확실하니까 for문으로 접근하자
for _ in range(t):
    for i in range(n):
        balls[i][0] += balls[i][1]

        # 벽에 닿을 경우
        if balls[i][0] == 0 or balls[i][0] == l:
            balls[i][1] *= -1

    # 충돌 체크
    pos_count = {}
    for i in range(n):
        pos = balls[i][0]
        if pos not in pos_count:
            pos_count[pos] = []
        # 인덱스들을 담아둡시다
        pos_count[pos].append(i)

    for pos in pos_count:
        if len(pos_count[pos]) > 1:
            ans += 1
            for idx in pos_count[pos]:
                # 충돌이 일어난 애들은 방향을 반전
                balls[idx][1] *= -1

print(ans)
