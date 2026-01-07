import sys

total = 0
N,M = map(int, sys.stdin.readline().split())
words = set(sys.stdin.readline() for _ in range(N))
check = list(sys.stdin.readline() for _ in range(M))

for i in check:
  if(i in words):
    total += 1

print(total)