def is_range(ny, nx):
    if 0 <= ny < 8 and 0 <= nx < 8:
        return True
    else:
        return False


def is_dol(ny, nx):
    if (ny, nx) == (d_cy, d_cx):
        return True
    else:
        return False

    ###################################


king, dol, n = input().split()
command = [input() for _ in range(int(n))]
###################################
grid = [[0] * 8 for _ in range(8)]

col_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
row_dict = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7}
cmd_dict = {"R": 0, "L": 1, "B": 2, "T": 3, "RT": 4, "LT": 5, "RB": 6, "LB": 7}

king_y, king_x, dol_y, dol_x = row_dict[king[1]], col_dict[king[0]], row_dict[dol[1]], col_dict[dol[0]]

grid[king_y][king_x] = 1
grid[dol_y][dol_x] = 2
###################################
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, -1, -1, 1, 1]

k_cy, k_cx = king_y, king_x
d_cy, d_cx = dol_y, dol_x
for cmd in command:
    k_ny, k_nx = k_cy + dy[cmd_dict[cmd]], k_cx + dx[cmd_dict[cmd]]
    if is_range(k_ny, k_nx):
        if is_dol(k_ny, k_nx):
            d_ny, d_nx = d_cy + dy[cmd_dict[cmd]], d_cx + dx[cmd_dict[cmd]]
            if is_range(d_ny, d_nx):
                grid[k_cy][k_cx] = 0
                grid[k_ny][k_nx] = 1
                grid[d_ny][d_nx] = 2
                k_cy, k_cx = k_ny, k_nx
                d_cy, d_cx = d_ny, d_nx
        else:
            grid[k_cy][k_cx] = 0
            grid[k_ny][k_nx] = 1
            k_cy, k_cx = k_ny, k_nx

###################################
# 왕, 돌 위치 찾기
res_king = ""
res_dol = ""

col_dict = dict(map(reversed, col_dict.items()))
row_dict = dict(map(reversed, row_dict.items()))

for row in range(8):
    for col in range(8):
        if grid[row][col] == 1:
            res_king += col_dict[col]
            res_king += row_dict[row]

        elif grid[row][col] == 2:
            res_dol += col_dict[col]
            res_dol += row_dict[row]

print(res_king)
print(res_dol)
