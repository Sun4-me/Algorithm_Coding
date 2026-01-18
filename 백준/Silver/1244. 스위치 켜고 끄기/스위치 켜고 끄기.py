n = int(input())
arr = list(map(int, input().split()))


def switch(arr, num):
    if arr[num] == 0:
        arr[num] = 1
    else:
        arr[num] = 0


k = int(input())
for _ in range(k):
    x, num = map(int, input().split())

    if x == 1:
        for i in range(num - 1, n, num):
            switch(arr, i)

    else:
        idx = num - 1
        switch(arr, idx)
        left = idx - 1
        right = idx + 1
        while left >= 0 and right < n and arr[left] == arr[right]:
            switch(arr, left)
            switch(arr, right)
            left -= 1
            right += 1


for i in range(0, n, 20):
    print(*arr[i : i + 20])
