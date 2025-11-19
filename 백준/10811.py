import sys

N, M = map(int,sys.stdin.readline().split())
list_int = [0] * N

for i in range(N):
  list_int[i] = i + 1 

for i in range(M):
  a,b = map(int,sys.stdin.readline().split())
  while(a < b):
    list_int[a-1],list_int[b-1] = list_int[b-1],list_int[a-1]
    a += 1
    b -= 1

for i in range(N):
  print(list_int[i], end=" ") 
