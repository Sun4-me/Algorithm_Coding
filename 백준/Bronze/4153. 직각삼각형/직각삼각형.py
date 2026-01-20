while True:
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break

    max_nums = max(nums)
    nums.remove(max_nums)

    if max_nums ** 2 == nums[0] ** 2 + nums[1] ** 2:
        print("right")
    else:
        print("wrong")
