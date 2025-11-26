import sys

a = [1,1,2,2,2,8]

list_int = list(map(int,sys.stdin.readline().split()))

for i in range(len(list_int)):
  print(a[i] - list_int[i], end=" ")