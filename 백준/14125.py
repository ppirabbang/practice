import sys

a = sorted(list(map(int,sys.stdin.readline().split())))

if(a[2] < a[0] + a[1]):
  print(sum(a))
else:
  print((a[0] + a[1]) * 2 - 1)