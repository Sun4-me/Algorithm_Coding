def merge_sort(lst):
    length = len(lst)

    if length <= 1:
        return lst

    pivot = length // 2

    # 분할
    left = merge_sort(lst[:pivot])
    right = merge_sort(lst[pivot:])

    # 정복
    return merge(left, right)


def merge(left, right):
    i, j, lst = 0, 0, []

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            lst.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            j += 1

    lst += right[j:]
    lst += left[i:]

    return lst


n = int(input())
nums = [int(input()) for _ in range(n)]

res = merge_sort(nums)

for i in res:
    print(i)
