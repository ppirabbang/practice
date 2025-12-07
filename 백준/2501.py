import sys

a, b = map(int, sys.stdin.readline().split())
list_int = []

for i in range(1,a+1):
  if(a % i == 0):
    list_int.append(i)


if(len(list_int) >= b):
  print(list_int[b-1])
else:
  print(0)
