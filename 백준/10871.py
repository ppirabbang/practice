import sys

N,X = map(int,sys.stdin.readline().split())

list_int = list(map(int, sys.stdin.readline().split()))

for i in list_int:
  if(X > i):
    print(i, end=" ")