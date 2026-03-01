t = int(input())
for _ in range(t):
    all_animals = list(input().split())
    not_fox = set()
    while True:
        line = list(input().split())
        if line == ['what', 'does', 'the', 'fox', 'say?']:
            break
        not_fox.add(line[-1])

    for i in all_animals:
        if i not in not_fox:
            print(i, end=" ")
