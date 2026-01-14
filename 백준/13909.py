import sys

N = int(sys.stdin.readline())
count = 0

for i in range(1,int(N ** 0.5) + 1):
  count += 1
print(count)