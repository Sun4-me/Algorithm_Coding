li = list(map(int, input().split()))
ascending = [1, 2, 3, 4, 5, 6, 7, 8]

if li == ascending:
    print("ascending")
elif li == ascending[::-1]:
    print("descending")
else:
    print("mixed")
