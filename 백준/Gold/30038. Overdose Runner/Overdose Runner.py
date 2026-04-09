# 플레이어 p, 빈칸 ., 몬스터 m, 장애물 *, 목적지 g
# 플레이어
# 공격력, 공격 사거리, 이동속도, 레벨 , 경험치, 요구 경험치

# [순간 이동]
# 행동력 1 소모
# 상하좌우 한 방향으로 이동속도 만큼 떨어진 위치로 이동
# 범위 밖이거나, 장애물, 몬스터이면 못 감

# [대기]
# 행동력 1 소모

# [공격]
# 행동력 3 소모
# 상하좌우중 한 방향으로 투사체 발사
# 공격 사거리 만큼의 거리를 한 칸씩 움직임
# 움직일 다음 좌표에 장애물이 있으면 사라짐
# 다음 좌표에 몬스터 있으면
# 플레이어 공격력 - 몬스터 방어력 만큼 몬스터 체력 감소
# 공격력이 방어력 보다 낮으면 체력 감소 x
# 몬스터 체력 0이하 되면 빈칸이 되고 플레이어 경험치 흭득

# [약먹기]
# 행동력 2 소모
# 이동속도 1 증가 혹은 감소
# 이동속도가 0인 경우 음수로 내려가지 않고 행동력은 소모 됨
# 약을 5번 먹을 때마다 overdose상태가 됨
# overdose상태에서는 순간이동, 대기만 가능함
# 행동력 10이상 소모한 경우 overdose해제됨
# 플레이어가 목적지랑 같은 좌표에 있으면 클리어되고 다른행동 x

# [경험치 흭득]
# 경험치를 얻고 요구 경험치 이상이되면
# 경험치 < 요구경험치를 만족할 때까지 레벨이 상승하고
# 경험치를 요구 경험치 만큼 뺌

# [레벨 상승]
# l 레벨에서 레벨 상승 시
# 레벨 l+1, 공격력 + l, 공격 사거리 +1, 요구 경험치 + 10

# [명령 처리]
# 불가능 한 행동일 경우 행동 무시
from collections import defaultdict

# -----------------------------------------------------
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def inb(y, x):
    return 0 <= y < N and 0 <= x < M


# -----------------------------------------------------

def teleport(d):
    global amount, py, px

    dist = player[2]
    ny, nx = py + (dy[d] * dist), px + (dx[d] * dist)

    if not inb(ny, nx): return
    if grid[ny][nx] not in ('.', 'p'): return

    # 이동
    amount += 1
    grid[py][px] = '.'
    grid[ny][nx] = 'p'
    py, px = ny, nx

    if player[7]:
        player[7] -= 1
    return


# -----------------------------------------------------

def wait():
    global amount
    amount += 1
    if player[7]:
        player[7] -= 1
    return


# -----------------------------------------------------

def attack(d):
    global amount

    amount += 3

    target_coord = []

    dist = player[1]
    power = player[0]

    ny, nx = py, px
    for _ in range(dist):
        ny, nx = ny + dy[d], nx + dx[d]
        if not inb(ny, nx): break
        if grid[ny][nx] == '*': break
        target_coord.append((ny, nx))

    for y, x in target_coord:
        if grid[y][x] != '.':
            hp, defence, experience = monster[grid[y][x]]
            if power - defence >= 0:
                monster[grid[y][x]][0] -= (power - defence)
                if monster[grid[y][x]][0] <= 0:
                    grid[y][x] = '.'
                    player[4] += experience

    level_up()


# -----------------------------------------------------

def level_up():
    now_level = player[5]
    need_exp, now_exp = player[3], player[4]

    if now_exp >= need_exp:
        while True:
            if now_exp < need_exp: break
            now_exp -= need_exp

            player[5] += 1
            player[0] += now_level
            player[1] += 1
            player[3] += 10
            player[4] = now_exp

            now_level += 1
            need_exp = player[3]



# -----------------------------------------------------

def medicine(k):
    global amount

    amount += 2
    player[2] = max(0, player[2] + k)
    player[6] += 1
    if player[6] == 5:
        player[6] = 0
        player[7] = 10


# -----------------------------------------------------

def clear():
    if (py, px) == (gy, gx):
        return True
    return False


# -----------------------------------------------------
N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
# 몬스터 번호: 체력, 방어력, 경험치
monster = defaultdict(list)
k = int(input())
line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))
for num in range(1, k + 1):
    monster[str(num)].append(line1[num - 1])
    monster[str(num)].append(line2[num - 1])
    monster[str(num)].append(line3[num - 1])

s = int(input())
command = list(input().split())
# 0공격력, 1공격사거리, 2이동속도, 3요구경험치,
# 4경험치, 5레벨, 6약 먹은 횟수, 7OVERDOSE 상태 시 10
player = [5, 1, 1, 10, 0, 1, 0, 0]

# -----------------------------------------------------
py, px = -1, -1
gy, gx = -1, -1
idx = 1

for y in range(N):
    for x in range(M):
        if grid[y][x] == 'm':
            grid[y][x] = str(idx)
            idx += 1
        elif grid[y][x] == 'p':
            py, px = y, x
        elif grid[y][x] == 'g':
            gy, gx = y, x
            grid[y][x] = '.'
# -----------------------------------------------------
amount = 0
for cmd in command:
    if player[7]:
        if cmd == 'u':
            teleport(0)
        elif cmd == 'd':
            teleport(1)
        elif cmd == 'l':
            teleport(2)
        elif cmd == 'r':
            teleport(3)
        elif cmd == 'w':
            wait()
    else:
        if cmd == 'u':
            teleport(0)
        elif cmd == 'd':
            teleport(1)
        elif cmd == 'l':
            teleport(2)
        elif cmd == 'r':
            teleport(3)
        elif cmd == 'w':
            wait()
        elif cmd == 'au':
            attack(0)
        elif cmd == 'ad':
            attack(1)
        elif cmd == 'al':
            attack(2)
        elif cmd == 'ar':
            attack(3)
        elif cmd == 'du':
            medicine(1)
        elif cmd == 'dd':
            medicine(-1)
        elif cmd == 'c':
            if clear(): break

if grid[gy][gx] == '.':
    grid[gy][gx] = 'g'

for y in range(N):
    for x in range(M):
        if grid[y][x] not in ('*', '.', 'p', 'g'):
            grid[y][x] = 'm'

print(player[5], player[4])
print(amount)
for row in grid:
    print(*row, sep="")
for val in monster.values():
    if val[0] > 0:
        print(val[0], end=" ")
