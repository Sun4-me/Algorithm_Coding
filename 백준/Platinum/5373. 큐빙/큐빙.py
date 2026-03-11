from collections import deque


def rotate_L(dir):
    k = 3
    dices[k].rotate(dir)

    # 윗면
    dices[0][0][0] = dices[k][0][0]
    dices[1][0][0] = dices[k][0][1]
    dices[2][0][0] = dices[k][0][2]

    # 앞면
    dices[6][1][0] = dices[k][1][0]
    dices[7][1][0] = dices[k][1][1]
    dices[8][1][0] = dices[k][1][2]

    # 아랫면
    dices[2][2][2] = dices[k][2][0]
    dices[1][2][2] = dices[k][2][1]
    dices[0][2][2] = dices[k][2][2]

    # 뒷면
    dices[8][3][2] = dices[k][3][0]
    dices[7][3][2] = dices[k][3][1]
    dices[6][3][2] = dices[k][3][2]

    transpose([0, 1, 2], 3, dir)
    transpose([6, 7, 8], 0, dir)


def rotate_R(dir):
    k = 5
    dices[k].rotate(-dir)

    # 윗면
    dices[0][0][2] = dices[k][0][0]
    dices[1][0][2] = dices[k][0][1]
    dices[2][0][2] = dices[k][0][2]

    # 앞면
    dices[6][1][2] = dices[k][1][0]
    dices[7][1][2] = dices[k][1][1]
    dices[8][1][2] = dices[k][1][2]

    # 아랫면
    dices[2][2][0] = dices[k][2][0]
    dices[1][2][0] = dices[k][2][1]
    dices[0][2][0] = dices[k][2][2]

    # 뒷면
    dices[8][3][0] = dices[k][3][0]
    dices[7][3][0] = dices[k][3][1]
    dices[6][3][0] = dices[k][3][2]

    transpose([0, 1, 2], 1, dir)
    transpose([6, 7, 8], 2, dir)


def rotate_B(dir):
    k = 0
    dices[k].rotate(-dir)

    # 윗면
    dices[3][0][0] = dices[k][0][0]
    dices[4][0][0] = dices[k][0][1]
    dices[5][0][0] = dices[k][0][2]

    # 오른쪽면
    dices[6][2][2] = dices[k][1][0]
    dices[7][2][2] = dices[k][1][1]
    dices[8][2][2] = dices[k][1][2]

    # 아랫면
    dices[5][2][2] = dices[k][2][0]
    dices[4][2][2] = dices[k][2][1]
    dices[3][2][2] = dices[k][2][2]

    # 왼쪽면
    dices[8][0][0] = dices[k][3][0]
    dices[7][0][0] = dices[k][3][1]
    dices[6][0][0] = dices[k][3][2]

    transpose([3, 4, 5], 3, -dir)
    transpose([6, 7, 8], 3, dir)


def rotate_F(dir):
    k = 2
    dices[k].rotate(dir)

    # 윗면
    dices[3][0][2] = dices[k][0][0]
    dices[4][0][2] = dices[k][0][1]
    dices[5][0][2] = dices[k][0][2]

    # 오른쪽면
    dices[6][2][0] = dices[k][1][0]
    dices[7][2][0] = dices[k][1][1]
    dices[8][2][0] = dices[k][1][2]

    # 아랫면
    dices[5][2][0] = dices[k][2][0]
    dices[4][2][0] = dices[k][2][1]
    dices[3][2][0] = dices[k][2][2]

    # 왼쪽면
    dices[8][0][2] = dices[k][3][0]
    dices[7][0][2] = dices[k][3][1]
    dices[6][0][2] = dices[k][3][2]

    transpose([3, 4, 5], 1, -dir)
    transpose([6, 7, 8], 1, dir)


def rotate_U(dir):
    k = 6
    dices[k].rotate(-dir)

    # 왼쪽면
    dices[0][3][2] = dices[k][0][0]
    dices[1][3][2] = dices[k][0][1]
    dices[2][3][2] = dices[k][0][2]

    # 앞면
    dices[3][1][0] = dices[k][1][0]
    dices[4][1][0] = dices[k][1][1]
    dices[5][1][0] = dices[k][1][2]

    # 오른쪽면
    dices[2][1][0] = dices[k][2][0]
    dices[1][1][0] = dices[k][2][1]
    dices[0][1][0] = dices[k][2][2]

    # 뒷면
    dices[5][3][2] = dices[k][3][0]
    dices[4][3][2] = dices[k][3][1]
    dices[3][3][2] = dices[k][3][2]

    transpose([0, 1, 2], 0, dir)
    transpose([3, 4, 5], 0, -dir)


def rotate_D(dir):
    k = 8
    dices[k].rotate(dir)

    # 왼쪽면
    dices[0][3][0] = dices[k][0][0]
    dices[1][3][0] = dices[k][0][1]
    dices[2][3][0] = dices[k][0][2]

    # 앞면
    dices[3][1][2] = dices[k][1][0]
    dices[4][1][2] = dices[k][1][1]
    dices[5][1][2] = dices[k][1][2]

    # 오른쪽면
    dices[2][1][2] = dices[k][2][0]
    dices[1][1][2] = dices[k][2][1]
    dices[0][1][2] = dices[k][2][2]

    # 뒷면
    dices[5][3][0] = dices[k][3][0]
    dices[4][3][0] = dices[k][3][1]
    dices[3][3][0] = dices[k][3][2]

    transpose([0, 1, 2], 2, dir)
    transpose([3, 4, 5], 2, -dir)


def transpose(idx_lst, num, dir):
    tmp = []

    for i in idx_lst:
        tmp.append(dices[i][num])

    if dir == 1:
        tmp = [lst[::-1] for lst in list(map(list, zip(*tmp)))]
    elif dir == -1:
        tmp = [lst for lst in list(map(list, zip(*tmp)))[::-1]]

    step = 0

    for i in idx_lst:
        dices[i][num] = tmp[step]
        step += 1


T = int(input())
for _ in range(T):
    dices = [
        # 윗면(하양), 오른쪽면(파랑), 아랫면(노랑), 왼쪽면(초록)
        # 0: [B]: 뒷면
        deque([['w', 'w', 'w'], ['b', 'b', 'b'], ['y', 'y', 'y'], ['g', 'g', 'g']]),
        # 1: 가운데
        deque([['w', 'w', 'w'], ['b', 'b', 'b'], ['y', 'y', 'y'], ['g', 'g', 'g']]),
        # 2: [F]: 앞면
        deque([['w', 'w', 'w'], ['b', 'b', 'b'], ['y', 'y', 'y'], ['g', 'g', 'g']]),

        # 윗면(하양), 앞면(빨강), 아랫면(노랑), 뒷면(오렌지)
        # 3: [L]: 왼쪽면
        deque([['w', 'w', 'w'], ['r', 'r', 'r'], ['y', 'y', 'y'], ['o', 'o', 'o']]),
        # 4: 가운데
        deque([['w', 'w', 'w'], ['r', 'r', 'r'], ['y', 'y', 'y'], ['o', 'o', 'o']]),
        # 5: [R]: 오른쪽면
        deque([['w', 'w', 'w'], ['r', 'r', 'r'], ['y', 'y', 'y'], ['o', 'o', 'o']]),

        # 왼쪽면(초록), 앞면(빨강), 오른쪽면(파랑), 뒷면(오렌지)
        # 6: [U]: 윗면
        deque([['g', 'g', 'g'], ['r', 'r', 'r'], ['b', 'b', 'b'], ['o', 'o', 'o']]),
        # 7: 가운데
        deque([['g', 'g', 'g'], ['r', 'r', 'r'], ['b', 'b', 'b'], ['o', 'o', 'o']]),
        # 8: [D]: 아랫면
        deque([['g', 'g', 'g'], ['r', 'r', 'r'], ['b', 'b', 'b'], ['o', 'o', 'o']])
    ]

    N = int(input())
    command = list(input().split())

    for cmd in command:
        a, b = cmd[:1], cmd[1:]
        if b == '-':
            b = -1

        elif b == '+':
            b = 1

        if a == 'U':
            rotate_U(b)

        elif a == 'D':
            rotate_D(b)

        elif a == 'F':
            rotate_F(b)

        elif a == 'B':
            rotate_B(b)

        elif a == 'L':
            rotate_L(b)

        elif a == 'R':
            rotate_R(b)

    print(*dices[0][0], sep="")
    print(*dices[1][0], sep="")
    print(*dices[2][0], sep="")
