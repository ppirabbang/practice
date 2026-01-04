import sys

N = int(sys.stdin.readline())
list_int = []

for i in range(N):
  x,y = map(int,sys.stdin.readline().split())
  list_int.append((x,y))
  
list_int.sort(key=lambda x : x[1])

for i in list_int:
  print(i[0],i[1])