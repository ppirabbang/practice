import sys

N,k = map(int,sys.stdin.readline().split())
list_int = list(map(int,sys.stdin.readline().split()))

list_int.sort()
print(list_int[(len(list_int) -k)])