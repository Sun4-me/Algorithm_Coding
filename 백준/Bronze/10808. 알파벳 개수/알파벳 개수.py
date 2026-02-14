import sys

s = sys.stdin.readline().strip()
alphabet_counts = [0] * 26

for char in s:
    alphabet_counts[ord(char) - ord('a')] += 1

print(*alphabet_counts)
