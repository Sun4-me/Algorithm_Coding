li = [input() for _ in range(3)]

max_num = 0

for i in li:
    if i.isdigit():
        max_num = i


def FizzBuzz(idx):
    if idx % 3 == 0 and idx % 5 == 0:
        return "FizzBuzz"
    elif idx % 3 == 0 and idx % 5 != 0:
        return "Fizz"
    elif idx % 3 != 0 and idx % 5 == 0:
        return "Buzz"
    else:
        return idx


if li.index(max_num) == 2:
    idx = int(max_num) + 1
    print(FizzBuzz(idx))

elif li.index(max_num) == 1:
    idx = int(max_num) + 2
    print(FizzBuzz(idx))

else:
    idx = int(max_num) + 3
    print(FizzBuzz(idx))
