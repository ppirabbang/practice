import sys

N = int(sys.stdin.readline())
list_int = [int(sys.stdin.readline()) for _ in range(N)]


list_int.sort()

for i in list_int:
  print(i)