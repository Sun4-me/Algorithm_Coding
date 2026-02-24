# 슬라이싱으로 풀어보기

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

for cmd in commands:
    if cmd == 1:
        n_arr = [lst for lst in arr[::-1]]
    elif cmd == 2:
        n_arr = [lst[::-1] for lst in arr]
    elif cmd == 3:
        n_arr = [lst[::-1] for lst in list(map(list, zip(*arr)))]
        n, m = m, n
    elif cmd == 4:
        n_arr = [lst for lst in list(map(list, zip(*arr)))[::-1]]
        n, m = m, n
    else:
        n_arr = []
        n2, m2 = n // 2, m // 2
        arr1 = [lst[:m2] for lst in arr[:n2]]
        arr2 = [lst[m2:] for lst in arr[:n2]]
        arr3 = [lst[m2:] for lst in arr[n2:]]
        arr4 = [lst[:m2] for lst in arr[n2:]]

        if cmd == 5:
            for lst1, lst2 in zip(arr4, arr1):
                n_arr.append(lst1 + lst2)
            for lst1, lst2 in zip(arr3, arr2):
                n_arr.append(lst1 + lst2)

        else:
            for lst1, lst2 in zip(arr2, arr3):
                n_arr.append(lst1 + lst2)
            for lst1, lst2 in zip(arr1, arr4):
                n_arr.append(lst1 + lst2)

    arr = n_arr

for lst in arr:
    print(*lst)
