import sys


def recur(n, y, x, k):
    if n == 0:
        print(k)
        sys.exit()

    half = (2 ** (n - 1))

    if y < half:
        if x < half:  # 1사분면
            return recur(n - 1, y, x, k)
        elif x >= half:  # 2사분면
            return recur(n - 1, y, x - half, k + (2 ** (n - 1)) ** 2)


    else:
        if x < half:  # 3사분면
            return recur(n - 1, y - half, x, k + ((2 ** (n - 1)) ** 2) * 2)

        elif x >= half:  # 4사분면
            return recur(n - 1, y - half, x - half, k + ((2 ** (n - 1)) ** 2) * 3)


#################################################
N, r, c = map(int, input().split())
#################################################
recur(N, r, c, 0)
