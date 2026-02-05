def divide(arr):
    global white, blue
    color = is_colored(arr)
    if color == 1:
        white += 1
        return
    elif color == 2:
        blue += 1
        return

    # 다른 색이 섞여있는 경우
    # 1, 2
    # 3, 4
    length = len(arr) // 2
    arr_1 = [row[:length] for row in arr[:length]]
    arr_2 = [row[length:] for row in arr[:length]]
    arr_3 = [row[:length] for row in arr[length:]]
    arr_4 = [row[length:] for row in arr[length:]]

    divide(arr_1)
    divide(arr_2)
    divide(arr_3)
    divide(arr_4)


def is_colored(arr):
    one = 0  # 1은 파란색
    zero = 0  # 0은 흰색
    for row in range(len(arr)):
        for col in range(len(arr)):
            if arr[row][col] == 0:
                zero += 1
            else:
                one += 1

            if one >= 1 and zero >= 1:
                return 0  # 다른 색 섞여 있음 / 더 확인 할 필요 X

    return 1 if one == 0 else 2
    # 리턴이 0이면 다른색 섞여 있음, 1이면 흰색, 2면 파란색임


# 정사각형 하얀색 or 파란색
# N**2일 경우..
# 같은 색으로 칠해져있지 않으면 똑같은 크기의 4개로 나눔
# 이후 각각에 대해서도 같은색으로 나누어질때까지 반복
# 하얀색 0, 파란색 1
# 각각의 개수 구하기
n = int(input())
gird = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0

divide(gird)

print(white)
print(blue)
