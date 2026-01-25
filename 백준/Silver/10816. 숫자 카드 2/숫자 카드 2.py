import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))

count_dict = {}

for card in cards:
    if card in count_dict:
        count_dict[card] += 1
    else:
        count_dict[card] = 1

for num in search:
    print(count_dict.get(num, 0), end=" ")
