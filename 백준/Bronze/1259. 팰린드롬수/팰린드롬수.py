while True:
    k = input()

    if k == '0':
        break

    if k == k[::-1]:
        print("yes")
    else:
        print("no")
