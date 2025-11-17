import sys

N,M = map(int,sys.stdin.readline().split())

list_int = [0] * N
for i in range(M):
  first,last,ball = map(int,sys.stdin.readline().split())

  for k in range(first,last+1):
    list_int[k-1] = ball

for i in range(N):
  print(list_int[i], end=" ")