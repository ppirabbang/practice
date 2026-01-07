import sys

N = int(sys.stdin.readline())
list_N = set(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
list_M = list(map(int,sys.stdin.readline().split()))

for i in list_M:
  if i in list_N:
    print(1, end=" ")
  else:
    print(0, end=" ")