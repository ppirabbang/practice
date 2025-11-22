import sys

s = sys.stdin.readline().rstrip()

for c in range(26):
    print(s.find(chr(ord('a') + c)), end=' ')
