import sys

N = int(sys.stdin.readline())
sum = 0
list_float = list(map(float,sys.stdin.readline().split()))

maximum = max(list_float)

for i in range(N):
  sum += list_float[i]/maximum * 100

print(sum/N)
