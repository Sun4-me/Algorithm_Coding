import sys

input = sys.stdin.readline

n = int(input())
current_people = set()

for _ in range(n):
    person, log = input().split()

    if log == "enter":
        current_people.add(person)

    else:
        current_people.remove(person)

res = list(current_people)
res.sort(reverse=True)

for i in res:
    print(i)
