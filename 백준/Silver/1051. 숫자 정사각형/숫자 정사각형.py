n, m = map(int, input().split())
grid = [list(map(int, input())) for _ in range(n)]

max_size = 1

for row in range(n):
    for col in range(m):
        for offset in range(1, 50):
            current_num = grid[row][col]
            if row + offset > n - 1 or col + offset > m - 1:
                break

            right = grid[row][col + offset]
            down = grid[row + offset][col]
            right_down = grid[row + offset][col + offset]

            if current_num == right == down == right_down:
                current_size = (offset + 1) ** 2
                if current_size > max_size:
                    max_size = current_size
print(max_size)
